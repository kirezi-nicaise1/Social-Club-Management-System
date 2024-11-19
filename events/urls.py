from django.urls import path
from .views import event_list, event_create, event_update, event_delete,view_attendees
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', event_list, name='event_list'),  
    path('create/', event_create, name='event_create'), 
    path('update/<int:pk>/', event_update, name='event_update'), 
    path('delete/<int:pk>/', event_delete, name='event_delete'), 
    path('<int:event_id>/attendees/', view_attendees, name='view_attendees'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
 
]
