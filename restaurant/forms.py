from django import forms
from .models import Booking

# Code added for loading form data on the Booking page
class BookingForm(forms.ModelForm):
    booking_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
            }
        )
    )
    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'booking_date']
        labels = {'booking_date': ''}