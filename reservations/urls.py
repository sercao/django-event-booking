from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/new/', views.event_new, name='event_new'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('event/<int:event_pk>/reservations/new/', views.reservation_new, name='reservation_new'),
    path('reservation/<int:pk>/edit/', views.reservation_edit, name='reservation_edit'),
    path('reservation/<int:pk>/delete/', views.reservation_delete, name='reservation_delete'),
]
