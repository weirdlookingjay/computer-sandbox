# monitoring/api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as drf_status
from django.utils import timezone
from .serializers import PingSerializer, AgentSerializer
from .models import Agent
import requests

class PingView(APIView):
    def get(self, request):
        serializer = PingSerializer({"status": "ok"})
        return Response(serializer.data)

class AgentListView(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class AgentStatusView(APIView):
    def get(self, request, pk):
        try:
            agent = Agent.objects.get(pk=pk)
        except Agent.DoesNotExist:
            return Response({"detail": "Agent not found."}, status=drf_status.HTTP_404_NOT_FOUND)

        url = f"http://{agent.ip_address}:8001/status"
        headers = {"Authorization": f"Bearer {agent.token}"}
        try:
            resp = requests.get(url, headers=headers, timeout=3)
            resp.raise_for_status()
            data = resp.json()
            # Update agent last_seen and status
            agent.last_seen = timezone.now()
            agent.status = "online"
            agent.save(update_fields=["last_seen", "status"])
            return Response(data)
        except requests.RequestException as e:
            agent.status = "offline"
            agent.save(update_fields=["status"])
            return Response({"detail": "Agent unreachable", "error": str(e)}, status=drf_status.HTTP_503_SERVICE_UNAVAILABLE)

