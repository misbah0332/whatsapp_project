# employee_register/views.py
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from .models import WhatsAppMessage

def incoming_whatsapp_message(request):
    # Get the message details
    from_number = request.POST.get('From')
    to_number = request.POST.get('To')
    body = request.POST.get('Body')

    # Save the message to the database
    WhatsAppMessage.objects.create(from_number=from_number, to_number=to_number, body=body)

    # Respond to the message (optional)
    response = MessagingResponse()
    response.message("Thank you for your message!")

    return HttpResponse(str(response), content_type='text/xml')
