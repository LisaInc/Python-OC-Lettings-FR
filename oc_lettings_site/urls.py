from django.contrib import admin
from django.urls import path, include

from .views import index
import lettings.urls
import profiles.urls


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("", index, name="index"),
    path("lettings/", include(lettings.urls, "lettings")),
    path("profiles/", include(profiles.urls, "profiles")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]
