# employee_register/urls.py
from django.urls import path
from .views import incoming_whatsapp_message

urlpatterns = [
    path('whatsapp/', incoming_whatsapp_message, name='incoming_whatsapp'),
]
