from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    bio = models.TextField(blank=True)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('follower, following') #prevents duplicate follows

    def __str__(self):
        return f'{self.username}'




