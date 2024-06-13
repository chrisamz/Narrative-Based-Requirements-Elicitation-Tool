# app/models.py

from django.db import models
from django.conf import settings

class Story(models.Model):
    """
    Model to store stories provided by stakeholders for requirements elicitation.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
