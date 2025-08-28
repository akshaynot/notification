from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['notif_type', 'mobile_no', 'email', 'scenario', 'subject', 'message']
        widgets = {
            'notif_type': forms.RadioSelect(choices=Notification.NOTIF_TYPE_CHOICES),
            'scenario': forms.Select(choices=Notification.SCENARIO_CHOICES),
        }
