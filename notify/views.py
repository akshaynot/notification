from django.shortcuts import render, redirect, get_object_or_404
from .models import Notification
from .forms import NotificationForm

def notification_list(request):
    notifications = Notification.objects.all().order_by('-created')
    form = NotificationForm()
    editing = False
    notif_id = None
    # handle both Add (POST on list view) and "Cancel" after editing
    if request.method == "POST" and not request.GET.get('edit'):
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
    return render(request, 'notifications/notification_form.html', {
        'form': form,
        'notifications': notifications,
        'editing': editing,
        'notif_id': notif_id,
    })

def notification_update(request, pk):
    notif = get_object_or_404(Notification, pk=pk)
    editing = True
    notifications = Notification.objects.all().order_by('-created')
    if request.method == "POST":
        form = NotificationForm(request.POST, instance=notif)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
    else:
        form = NotificationForm(instance=notif)
    # Render with editing context for form toggle and Cancel button
    return render(request, 'notifications/notification_form.html', {
        'form': form,
        'notifications': notifications,
        'editing': editing,
        'notif_id': pk,
    })

def notification_delete(request, pk):
    notif = get_object_or_404(Notification, pk=pk)
    notif.delete()
    return redirect('notification_list')
