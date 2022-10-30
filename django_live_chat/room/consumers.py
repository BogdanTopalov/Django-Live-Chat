import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.utils import timezone

from core.models import User
from room.models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

        user = self.scope['user']
        username = 'Anonymous' if user.is_anonymous else user.username
        connection_message = f'{username} joined the room.'
        #
        # if not user.username:
        #     await self.create_user()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': '',
                'username': '',
                'room': '',
                'connection_message': connection_message
            }
        )

    async def disconnect(self, code):
        user = self.scope['user']
        username = 'Anonymous' if user.is_anonymous else user.username
        connection_message = f'{username} left the room.'

        await self.set_last_online(user.id)

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': '',
                'username': '',
                'room': '',
                'connection_message': connection_message
            }
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']
        connection_message = data['connection_message']

        if not connection_message:
            await self.save_message(room, username, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room,
                'connection_message': connection_message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']
        connection_message = event['connection_message']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room,
            'connection_message': connection_message,
        }))

    @sync_to_async
    def save_message(self, room, username, message):
        room = Room.objects.get(slug=room)
        user = User.objects.get(username=username)
        Message.objects.create(user=user, room=room, text=message)

    @sync_to_async
    def set_last_online(self, user_id):
        User.objects.filter(id=user_id).update(last_online=timezone.now())

    # @sync_to_async
    # def create_user(self):
    #     User.objects.create_user(username='Anonymous')
