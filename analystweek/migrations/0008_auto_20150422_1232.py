# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('analystweek', '0007_auto_20150422_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usermeeting',
            name='meeting_of',
            field=models.ManyToManyField(related_name='host', verbose_name=b'Wipro Leader', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usermeeting',
            name='meeting_with',
            field=models.ManyToManyField(related_name='attendee', verbose_name=b'Analyst', to=settings.AUTH_USER_MODEL),
        ),
    ]
