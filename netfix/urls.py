# netfix/urls.py

from django.contrib import admin
from django.urls import path, include

from users import views as users_views
from services import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('services/', include('services.urls')),
    path('users/', include('users.urls')),
]
