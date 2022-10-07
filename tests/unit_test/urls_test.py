import pytest
from django.urls import reverse
from django.test import TestCase

from profiles.models import Profile, User
from lettings.models import Address, Letting


@pytest.mark.django_db
class TestUrls(TestCase):
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
        user = User.objects.create_user(username="test_username")
        Profile.objects.create(user=user, favorite_city="testville")

    def test_url_index(self):
        self._test_url("index", "/")

    def test_url_lettings_index(self):
        self._test_url("lettings:index", "/lettings/")

    def test_url_letting(self):
        self._test_url("lettings:letting", "/lettings/1/", args=["1"])

    def test_url_profiles_index(self):
        self._test_url("profiles:index", "/profiles/")

    def test_url_profile(self):
        self._test_url("profiles:profile", "/profiles/test_username/", args=["test_username"])

    def _test_url(self, view_name, url_tested, args=None):
        url = reverse(view_name, args=args)
        assert url == url_tested
