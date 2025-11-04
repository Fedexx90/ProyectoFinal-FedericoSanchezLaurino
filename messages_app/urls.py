from django.urls import path
from . import views

app_name = 'messages_app'

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent'),
    path('send/', views.send_message, name='send_message'),
    path('detail/<int:pk>/', views.message_detail, name='message_detail'),
    path('delete/<int:pk>/', views.delete_message, name='delete_message'),
]
