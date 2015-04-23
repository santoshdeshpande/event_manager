# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analystweek', '0008_auto_20150422_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='show_in_profile',
            field=models.BooleanField(default=True),
        ),
    ]
