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

class Requirement(models.Model):
    """
    Model to store requirements extracted from stakeholder stories.
    """
    description = models.TextField()
    priority = models.CharField(max_length=50, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium')
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='requirements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class Relationship(models.Model):
    """
    Model to store relationships between requirements.
    """
    RELATIONSHIP_TYPES = [
        ('depends_on', 'Depends On'),
        ('conflicts_with', 'Conflicts With'),
        ('related_to', 'Related To'),
    ]

    source = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name='outgoing_relationships')
    target = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name='incoming_relationships')
    relationship_type = models.CharField(max_length=50, choices=RELATIONSHIP_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('source', 'target', 'relationship_type')

    def __str__(self):
        return f"{self.source} {self.relationship_type} {self.target}"
