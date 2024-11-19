from django.contrib import admin
from django.urls import path, include
from .views import home_page
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_page, name='home'),
    path('events/', include('events.urls')), 
    path('members/', include('membership.urls')), 
    path('authentication/',include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
