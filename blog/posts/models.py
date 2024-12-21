from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel


class Post(TimeStampedModel):
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
