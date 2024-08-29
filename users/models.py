# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    field_of_work = models.CharField(max_length=100, blank=True)
    
    FIELD_CHOICES = [
        ('Air Conditioner', 'Air Conditioner'),
        ('All in One', 'All in One'),
        ('Carpentry', 'Carpentry'),
        ('Electricity', 'Electricity'),
        ('Gardening', 'Gardening'),
        ('Home Machines', 'Home Machines'),
        ('Housekeeping', 'Housekeeping'),
        ('Interior Design', 'Interior Design'),
        ('Locks', 'Locks'),
        ('Painting', 'Painting'),
        ('Plumbing', 'Plumbing'),
        ('Water Heaters', 'Water Heaters'),
    ]
    
    field_of_work = models.CharField(max_length=100, choices=FIELD_CHOICES, blank=True)
    
    def is_company(self):
        return bool(self.field_of_work)
    
    def is_customer(self):
        return not self.is_company()

class RequestedService(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='requested_services')
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    service_time = models.IntegerField()  # in hours
    date_requested = models.DateTimeField(auto_now_add=True)

    def calculated_cost(self):
        return self.service.price_per_hour * self.service_time