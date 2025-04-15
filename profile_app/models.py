from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    bio = models.TextField(blank=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    @property
    def followers_count(self):
        # This method returns the number of followers for the user
        return self.user.followers.count()
    
    @property
    def following_count(self):
        # This method returns the number of users the user is following
        return self.user.following.count()

    
class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed_at = models.DateField(auto_now_add=True)

   
    class Meta:
        unique_together = ('follower', 'following') #prevents duplicate follows

    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'







