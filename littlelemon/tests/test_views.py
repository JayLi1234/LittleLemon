from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.renderers import JSONRenderer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Lemon Cake", price=20, inventory=100)
        Menu.objects.create(title="Chicken Cutlet", price=20, inventory=100)
        Menu.objects.create(title="Pork Chop", price=20, inventory=100)
    
    def test_getall(self):
        serialized_menu = MenuSerializer(Menu.objects.all(), many=True)
        api_response = self.client.get('/api/menu-items')

        result_expected = JSONRenderer().render(serialized_menu.data)
        self.assertEqual(api_response.content, result_expected)