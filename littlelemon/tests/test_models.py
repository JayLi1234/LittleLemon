from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class BookingTest(TestCase):
    def test_get_booking(self):
        booking = Booking.objects.create(name="John", no_of_guests=10, booking_date="2022-08-01")
        self.assertEqual(str(booking), "John : 2022-08-01")