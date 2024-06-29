

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    dietary_preferences = models.TextField(null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    health_goals = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
