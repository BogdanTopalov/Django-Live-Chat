from django.urls import path

from core.views import HomeView, RegisterUserView, LoginUserView, LogoutUserView, CreateRoomView


urlpatterns = [
    path('', HomeView.as_view(), name='home page'),
    path('register/', RegisterUserView.as_view(), name='register page'),
    path('login/', LoginUserView.as_view(), name='login page'),
    path('logout/', LogoutUserView.as_view(), name='logout page'),
    path('open-room/', CreateRoomView.as_view(), name='create room')
]
