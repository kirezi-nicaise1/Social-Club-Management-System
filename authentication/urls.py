from django.urls import path
from .views import register, login_user, logout_user

urlpatterns = [
    path('register/',register,name='sign_up'),
    path('login/', login_user, name="login_user"),
    path('logout', logout_user, name="logout"),
]