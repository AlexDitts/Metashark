from django.db import models
from django.contrib.auth.models import User


class Curator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='curator', null=True)
    phone = models.CharField(max_length=12, verbose_name='phone')

    def __str__(self):
        return self.user.username
