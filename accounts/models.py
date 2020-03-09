from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class userProfile(models.Model):
    user = models.ForeignKey(User, verbose_name='UserProfile', related_name='%(class)s_requests_created', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


    class Meta:
        app_label = 'accounts'
