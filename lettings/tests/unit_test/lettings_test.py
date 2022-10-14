from django.test import TestCase
from lettings.models import Letting, Address
import pytest


@pytest.mark.django_db
class LettingTestCase(TestCase):
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

    def test_create_Letting(self):
        letting = Letting.objects.get(id=1)
        self.assertEqual(letting.title, "titre")


@pytest.mark.django_db
class AddressTestCase(TestCase):
    def setUp(self):
        Address.objects.create(
            number=1,
            street="rue du test",
            city="testville",
            state="testland",
            zip_code="01000",
            country_iso_code="fr",
        )

    def test_create_address(self):
        address = Address.objects.get(id=1)
        self.assertEqual(address.city, "testville")
