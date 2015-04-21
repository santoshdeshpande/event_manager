# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analystweek', '0004_auto_20150419_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(null=True, upload_to=b'profiles', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile',
            field=models.TextField(null=True, blank=True),
        ),
    ]
