from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(max_length=150)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.id} | {self.first_name} {self.last_name}" 