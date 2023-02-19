from django.db import models
from django.utils import timezone

# Create your models here.
class ClientRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    requested_date = models.DateTimeField(default=timezone.now, verbose_name='Requested at:')

    def __str__(self):
        return f"Name:{self.name} | Email:{self.email}"
