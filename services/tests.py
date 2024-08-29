# services/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Service

class ServiceModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testcompany',
            email='test@company.com',
            password='testpass123',
            field_of_work='All in One'
        )
        self.service = Service.objects.create(
            name='Test Service',
            description='This is a test service',
            field='Plumbing',
            price_per_hour=50.00,
            company=self.user
        )

    def test_service_creation(self):
        self.assertEqual(self.service.name, 'Test Service')
        self.assertEqual(self.service.field, 'Plumbing')
        self.assertEqual(self.service.price_per_hour, 50.00)
        self.assertEqual(self.service.company, self.user)

class ServiceViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testcompany',
            email='test@company.com',
            password='testpass123',
            field_of_work='All in One'
        )
        self.service = Service.objects.create(
            name='Test Service',
            description='This is a test service',
            field='Plumbing',
            price_per_hour=50.00,
            company=self.user
        )

    def test_service_list_view(self):
        response = self.client.get(reverse('service_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Service')

    def test_service_detail_view(self):
        response = self.client.get(reverse('service_detail', args=[self.service.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Service')
        self.assertContains(response, 'This is a test service')
