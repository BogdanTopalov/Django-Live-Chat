from django.views.generic import ListView, DetailView

from room.models import Room, Message


class RoomsView(ListView):
    model = Room
    template_name = 'room/rooms.html'
    context_object_name = 'rooms'


class RoomView(DetailView):
    model = Room
    template_name = 'room/room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['messages'] = Message.objects.filter(room=self.object.id)
        return context
