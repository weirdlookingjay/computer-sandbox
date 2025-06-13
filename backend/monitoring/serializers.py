# monitoring/serializers.py
from rest_framework import serializers
from .models import Agent

class PingSerializer(serializers.Serializer):
    status = serializers.CharField()

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'name', 'ip_address', 'last_seen', 'status']

