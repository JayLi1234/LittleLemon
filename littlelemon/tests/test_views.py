from django.test import TestCase
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer
from rest_framework.renderers import JSONRenderer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Lemon Cake", price=20, inventory=100)
        Menu.objects.create(title="Chicken Cutlet", price=20, inventory=100)
        Menu.objects.create(title="Pork Chop", price=20, inventory=100)
    
    def test_getall(self):
        serialized_menu = MenuSerializer(Menu.objects.all(), many=True)
        result_expected = JSONRenderer().render(serialized_menu.data)

        api_response = self.client.get('/api/menu-items')

        self.assertEqual(api_response.content, result_expected)

class BookingViewTest(TestCase):
    def setUp(self):
        Booking.objects.create(name="John Doe", no_of_guests=4, booking_date="2023-08-22")
        Booking.objects.create(name="Jimmy Doe", no_of_guests=2, booking_date="2023-08-24")
        Booking.objects.create(name="Sana", no_of_guests=6, booking_date="2023-08-23")

    def test_getall(self):
        serialized_booking = BookingSerializer(Booking.objects.all(), many=True)
        result_expected = JSONRenderer().render(serialized_booking.data)

        api_response = self.client.get('/api/bookings/tables/')

        self.assertEqual(api_response.content, result_expected)

