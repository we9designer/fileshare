# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import File

from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta
from celery.schedules import crontab
from celery.task import periodic_task
from django.utils import timezone

@periodic_task(run_every=crontab(minute='*/10080'))
def delete_old_files():
    files = File.objects.all()

    for file in files:

        if file.expiration_date < timezone.now():
            file.delete()
    return "completed deleting files at {}".format(timezone.now())

@periodic_task(run_every=(timedelta(seconds=50000)), name='my_first_task')
def my_first_task():
	print('This is test message and celery is works...')