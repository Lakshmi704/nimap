from django.urls import path, include

urlpatterns = [
    path('', include('core.api_urls')),  # API endpoints
]
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # This will match the root URL
    # Add other URL patterns here
]
