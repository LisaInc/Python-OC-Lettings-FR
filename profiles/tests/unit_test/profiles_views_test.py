from django.test import TestCase
from django.test import Client
from profiles.models import User, Profile
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestProfileView(TestCase):
    client = Client()

    def setUp(self):
        user = User.objects.create_user(username='test_username')
        Profile.objects.create(user=user, favorite_city='testville')

    def test_index_profiles(self):
        response = self.client.get(reverse("profiles:index"))
        assert response.status_code == 200
        assert b'Profiles' in response.content

    def test_profile(self):
        response = self.client.get(reverse("profiles:profile", args=['test_username']))
        assert response.status_code == 200
        assert b'test_username' in response.content
