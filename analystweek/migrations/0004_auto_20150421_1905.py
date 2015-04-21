# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analystweek', '0003_auto_20150421_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default='hello', max_length=255),
            preserve_default=False,
        ),
    ]
