# event_booking/reservations/forms.py

from django import forms
from .models import Event, Reservation, Comment

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['event', 'user', 'seats']
#validation
    def clean_seats(self):
        seats = self.cleaned_data.get('seats')
        if seats <= 0:
            raise forms.ValidationError("The number of seats must be greater than zero.")
        return seats
#comment form    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']