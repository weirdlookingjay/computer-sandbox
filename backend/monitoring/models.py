from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    last_seen = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default="offline")
    token = models.CharField(max_length=255, help_text="Shared secret for authentication")

    def __str__(self):
        return f"{self.name} ({self.ip_address})"
