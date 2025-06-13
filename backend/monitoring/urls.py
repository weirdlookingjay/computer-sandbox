# monitoring/urls.py
from django.urls import path
from .api_views import PingView
from .api_views import AgentListView
from .api_views import AgentStatusView
urlpatterns = [
    path('ping/', PingView.as_view(), name='ping'),
    path('agents/', AgentListView.as_view(), name='agent-list'),
    path('agents/<int:pk>/status/', AgentStatusView.as_view(), name='agent-status'),
]
