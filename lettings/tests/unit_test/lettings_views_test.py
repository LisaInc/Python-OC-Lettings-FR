from django.test import TestCase
from django.test import Client
from lettings.models import Letting, Address
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestLettingView(TestCase):
    client = Client()

    def setUp(self):
        address = Address.objects.create(
            number=1,
            street="rue du test",
            city="testville",
            state="testland",
            zip_code="01000",
            country_iso_code="fr",
        )
        Letting.objects.create(title="titre", address=address)

    def test_index_lettings(self):
        response = self.client.get(reverse("lettings:index"))
        assert response.status_code == 200
        assert b"Lettings" in response.content

    def test_profile(self):
        response = self.client.get(reverse("lettings:letting", args=["1"]))
        assert response.status_code == 200
        assert b"titre" in response.content
