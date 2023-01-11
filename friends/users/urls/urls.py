from django.urls import path

from users.views import (
    CreateUserView,
    LoginView,
    logout_view
)


urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]