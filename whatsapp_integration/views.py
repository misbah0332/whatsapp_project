from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WhatsAppMessage

@csrf_exempt
def receive_whatsapp_message(request):
    if request.method == 'POST':
        from_number = request.POST.get('From', '')
        message_body = request.POST.get('Body', '')

        # Save the message in the database
        WhatsAppMessage.objects.create(
            from_number=from_number,
            message_body=message_body
        )
        return HttpResponse("Message received", status=200)
    return HttpResponse("Invalid request", status=400)
