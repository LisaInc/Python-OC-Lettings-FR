from ctypes import addressof
from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User
import pytest


@pytest.mark.django_db
class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='test')
        Profile.objects.create(user=user, favorite_city='testville')

    def test_create_Profile(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.user.username, "test")
