from django.urls import path

from core.views import HomeView, RegisterUserView, LoginUserView, LogoutUserView


urlpatterns = [
    path('', HomeView.as_view(), name='home page'),
    path('register/', RegisterUserView.as_view(), name='register page'),
    path('login/', LoginUserView.as_view(), name='login page'),
    path('logout/', LogoutUserView.as_view(), name='logout page'),
]
