from django.test import TestCase, Client
from django.urls import reverse
from .models import Event, Reservation
from django.contrib.auth.models import User

# Pruebas para modelos
class EventModelTest(TestCase):

    def setUp(self):
        self.event = Event.objects.create(name='Test Event', description='Test Description')

    def test_event_creation(self):
        self.assertEqual(self.event.name, 'Test Event')
        self.assertEqual(self.event.description, 'Test Description')

class ReservationModelTest(TestCase):

    def setUp(self):
        self.event = Event.objects.create(name='Test Event', description='Test Description')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.reservation = Reservation.objects.create(event=self.event, user=self.user, seats=2)

    def test_reservation_creation(self):
        self.assertEqual(self.reservation.event.name, 'Test Event')
        self.assertEqual(self.reservation.user.username, 'testuser')
        self.assertEqual(self.reservation.seats, 2)

# Pruebas para vistas
class EventViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.event = Event.objects.create(name='Test Event', description='Test Description')
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_event_list_view(self):
        response = self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')

    def test_event_detail_view(self):
        response = self.client.get(reverse('event_detail', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')

    def test_event_create_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('event_new'), {
            'name': 'New Event',
            'description': 'New Description',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Event.objects.last().name, 'New Event')

class ReservationViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.event = Event.objects.create(name='Test Event', description='Test Description')
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_reservation_create_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('reservation_new', args=[self.event.id]), {
            'event': self.event.id,
            'user': self.user.id,
            'seats': 2,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.last().seats, 2)
