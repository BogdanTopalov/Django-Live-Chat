from django.contrib.auth import login

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from core.forms import RegisterForm, CreateRoomForm
from core.models import User
from room.models import Message, Room


class HomeView(TemplateView):
    template_name = 'core/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        if self.request.user.is_authenticated:
            current_user = User.objects.get(id=self.request.user.id)
            user_rooms = Room.objects.filter(creator_id=self.request.user.id)

            context['user_rooms'] = user_rooms

            if Message.objects.filter(user=current_user):
                unread_messages = Message.objects.filter(
                    date_added__gt=current_user.last_online
                )
                context['unread_messages'] = unread_messages
                context['unread_messages_count'] = {
                    f"{room.id}": len([msg for msg in unread_messages if msg.room.id == room.id])
                    for room in user_rooms
                }
        return context


class RegisterUserView(CreateView):
    form_class = RegisterForm
    template_name = 'core/register_page.html'
    success_url = reverse_lazy('home page')

    def form_valid(self, *args, **kwargs):
        """ Login after register """
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class LoginUserView(LoginView):
    template_name = 'core/login_page.html'

    def get_success_url(self):
        return reverse_lazy('home page')


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('home page')


class CreateRoomView(CreateView):
    model = Room
    template_name = 'room/create_room_page.html'
    form_class = CreateRoomForm

    def form_valid(self, form):
        """ Set room creator. """
        if self.request.user.is_anonymous:
            current_user = User.objects.create_user(username='Anonymous')
        else:
            current_user = self.request.user

        form.instance.creator = current_user
        return super().form_valid(form)

    def get_success_url(self):
        """ Redirect to the newly-created room. """
        return reverse_lazy('room', kwargs={'slug': self.object.slug})
