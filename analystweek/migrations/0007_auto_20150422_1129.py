# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('analystweek', '0006_auto_20150422_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermeeting',
            name='meeting_of',
            field=models.ManyToManyField(related_name='host', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usermeeting',
            name='meeting_with',
            field=models.ManyToManyField(related_name='attendee', to=settings.AUTH_USER_MODEL),
        ),
    ]
