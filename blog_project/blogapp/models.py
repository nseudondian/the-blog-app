from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class post(models.Model):
    title = models.CharField(max_length = 25)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        self.title