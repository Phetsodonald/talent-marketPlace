from django.db import models
from users.models import User
from talent.models import TalentProfile

# Create your models here.
class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('quoted', 'Quoted'),
        ('accepted', 'Accepted'),
        ('paid', 'Paid'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organizer_bookings")
    talent = models.ForeignKey(TalentProfile, on_delete=models.CASCADE, related_name="talent_bookings")

    event_date = models.DateField()
    location = models.CharField(max_length=200)

    message = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)

    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    talent = models.ForeignKey(TalentProfile, on_delete=models.CASCADE)

    rating = models.IntegerField()
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)