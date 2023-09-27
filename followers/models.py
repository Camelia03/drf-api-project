from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
    """
    Like model, related to 'owner' and 'post'.
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']


    def __str__(self):
        return f'{self.owner} {self.followed}'