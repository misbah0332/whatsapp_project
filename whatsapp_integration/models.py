# employee_register/models.py
from django.db import models

class WhatsAppMessage(models.Model):
    from_number = models.CharField(max_length=20)
    to_number = models.CharField(max_length=20)
    body = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.from_number} at {self.received_at}'
