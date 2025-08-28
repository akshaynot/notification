from django.db import models

class Notification(models.Model):
    NOTIF_TYPE_CHOICES = [
        ('EMAIL', 'Email'),
        ('SMS', 'SMS'),
    ]
    SCENARIO_CHOICES = [
        ('failure', 'Failure'),
        ('success', 'Success'),
        ('info', 'Info'),
    ]

    notif_type = models.CharField(max_length=10, choices=NOTIF_TYPE_CHOICES)
    mobile_no = models.CharField(max_length=12, blank=True)
    email = models.EmailField(blank=True)
    scenario = models.CharField(max_length=10, choices=SCENARIO_CHOICES)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} ({self.notif_type})"
