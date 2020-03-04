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

"""
@periodic_task(run_every=(timedelta(seconds=5)), name='my_first_task')
def my_first_task():
	print('HELLO!!!!!!!!!!!!!!!!!!!')


@shared_task
def my_second_task():
    print('second task')


@shared_task
def my_third_task():
    print('third task')


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_file():
    return File.objects.count()


@shared_task
def rename_files(widget_id, name):
    w = File.objects.get(id=file_id)
    w.name = name
    w.save()
"""	