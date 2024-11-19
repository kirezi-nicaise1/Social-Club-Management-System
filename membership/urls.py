from django.urls import path
from .views import member_list, member_create, member_update, member_delete,view_events
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', member_list, name='member_list'),
    path('create/', member_create, name='member_create'),  
    path('update/<int:pk>/', member_update, name='member_update'), 
    path('delete/<int:pk>/', member_delete, name='member_delete'), 
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('<int:member_id>/events/', view_events, name='view_events'),

]
