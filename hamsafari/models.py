from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='static/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username






STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'), 
        ('cancelled', 'Cancelled'),
    ]
class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    date = models.DateTimeField()
    seats_available = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    
    def __str__(self):
        return f"Trip from {self.start_location} to {self.end_location} on {self.date}"



STATUS_CHOICESS= [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
class CompanionRequest(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companion_requests')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='companion_requests')
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICESS, default='pending')
    booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Companion request for trip from {self.start_location} to {self.end_location} on {self.date}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='bookings')
    date_booked = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking for {self.user.username} on {self.trip}"
