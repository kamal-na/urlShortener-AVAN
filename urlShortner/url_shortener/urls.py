from django.contrib import admin
from django.urls import path
from shorten_url.views import ShortenUrl, GetOriginalUrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:short_id>', GetOriginalUrl.as_view(), name='get_original_url'),
    path('shorten-url/', ShortenUrl.as_view(), name='shorten_url'),
]
