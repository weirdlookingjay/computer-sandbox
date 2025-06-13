# monitoring/serializers.py
from rest_framework import serializers

class PingSerializer(serializers.Serializer):
    status = serializers.CharField()
