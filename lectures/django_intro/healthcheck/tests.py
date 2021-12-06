from django.test import TestCase

from django.test import Client
from django.urls import reverse
# Create your tests here.



class HealthcheckTestCase(TestCase):
    client = Client()

    def test_status_response(self):
        response = self.client.get(
            reverse('check-status')
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"OK")
