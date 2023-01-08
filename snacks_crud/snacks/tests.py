from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snacks


class SnackTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.snack = Snacks.objects.create(
            name='Chips', description='tasty', owner=self.user, price=2.2)

    def test_string_representation(self):
        self.assertEqual(str(self.snack), 'Chips')

    def test_movie_name(self):
        self.assertEqual(f'{self.snack.name}', 'Chips')

    def test_movie_rating(self):
        self.assertEqual(f'{self.snack.description}', 'tasty')

    def test_price(self):
        self.assertEqual(f'{self.snack.price}', '2.2')

    def test_list_page_status_code(self):
        url = reverse("list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "snack_list.html")