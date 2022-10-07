from django.contrib import admin
from django.urls import path, include

from .views import index
import lettings.urls
import profiles.urls


urlpatterns = [
    path("", index, name="index"),
    path("lettings/", include(lettings.urls, 'lettings')),
    path("profiles/", include(profiles.urls, 'profiles')),
    path("admin/", admin.site.urls),
]
