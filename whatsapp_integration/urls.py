from django.urls import path
from . import views

urlpatterns = [
    path('webhook/', views.receive_whatsapp_message, name='whatsapp_webhook'),
]
