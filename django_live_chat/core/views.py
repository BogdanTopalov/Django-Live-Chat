from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from core.forms import RegisterForm


class HomeView(TemplateView):
    template_name = 'core/home_page.html'


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
