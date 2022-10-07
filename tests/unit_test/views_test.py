from django.test import TestCase
from django.test import Client
from django.test import TestCase
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestProfileView(TestCase):
    client = Client()

    def test_index(self):
        response = self.client.get(reverse("index"))
        assert response.status_code == 200
        assert b'Welcome to Holiday Homes' in response.content
