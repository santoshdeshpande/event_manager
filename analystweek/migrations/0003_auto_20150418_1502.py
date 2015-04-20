# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analystweek', '0002_auto_20150418_0608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting',
            options={'ordering': ('start_time', 'modified')},
        ),
        migrations.AddField(
            model_name='meeting',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
