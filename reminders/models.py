from django.db import models

# Create your models here.

class Reminder(models.Model):
    MESSAGE_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]

    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    reminder_method = models.CharField(max_length=10, choices=MESSAGE_CHOICES)

    def __str__(self):
        return f"{self.message[:50]}... on {self.date} at {self.time} via {self.reminder_method}"
