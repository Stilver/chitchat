from django.contrib.auth.models import User
from django.db import models


class Messages(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
