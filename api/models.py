from django.db import models
from django.utils import timezone


class Story(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def latest_update_days(self):
        now = timezone.now()
        delta = now - self.updated_at
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif delta.seconds // 3600 > 0:
            return f"{delta.seconds // 3600} hours ago"
        elif delta.seconds // 60 > 0:
            return f"{delta.seconds // 60} minutes ago"
        else:
            return f"{delta.seconds} seconds ago"

    def __str__(self):
        return self.title
