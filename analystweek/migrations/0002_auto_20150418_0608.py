# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analystweek', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting',
            options={'ordering': ('modified',)},
        ),
        migrations.AddField(
            model_name='meeting',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 6, 8, 54, 13170, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
