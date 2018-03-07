from django.db import models
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    vk = models.CharField(max_length=50, blank=True)
    telegram = models.CharField(max_length=50, blank=True)
