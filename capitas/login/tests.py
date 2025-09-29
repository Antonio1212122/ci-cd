
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthViewsTest(TestCase):
    def test_register_and_login_flow(self):
        # Register
        resp = self.client.post(reverse('register'), {
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'pass12345',
            'confirm_password': 'pass12345',
        })
        self.assertEqual(resp.status_code, 302)  # redirect to home

        # Now logged in, access home
        resp = self.client.get(reverse('home'))
        self.assertContains(resp, 'alice')
