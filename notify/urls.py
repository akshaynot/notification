from django.urls import path
from . import views

urlpatterns = [
    path('', views.notification_list, name='notification_list'),
    path('edit/<int:pk>/', views.notification_update, name='notification_update'),
    path('delete/<int:pk>/', views.notification_delete, name='notification_delete'),
]
