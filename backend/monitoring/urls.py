# monitoring/urls.py
from django.urls import path
from .api_views import PingView

urlpatterns = [
    path('ping/', PingView.as_view(), name='ping'),
]
