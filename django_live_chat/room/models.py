from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

from core.models import User


class Room(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True)
    date_added = models.DateTimeField(default=timezone.now)
