from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class File(models.Model):
    user = models.ForeignKey(User, verbose_name='User', related_name='users', on_delete=models.CASCADE)
    description = models.CharField('Description', max_length=200, null=True, blank=True)
    created_at = models.DateTimeField('Created on', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now_add=True)
    expiration_date = models.DateTimeField('Experience', auto_now_add=True)
    file = models.FileField('Archive', upload_to='upload/file')
    cover = models.ImageField('Cover', upload_to='upload/cover')


    class Meta:
        app_label = 'share'

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('file_list')

