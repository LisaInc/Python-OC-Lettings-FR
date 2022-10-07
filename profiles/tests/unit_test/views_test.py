from django.test import TestCase
from django.test import Client as Cli
from django.test import TestCase
from profiles.models import User, Profile
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestUsers(TestCase):
    client = Cli()

    def setUp(self):
        user = User.objects.create_user(username='test')
        Profile.objects.create(user=user, favorite_city='testville')

    def test_logout_user(self):
        response = self.client.get(reverse("profile:index"))
        assert response.url == "profiles/"
        assert response.status_code == 200
