# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analystweek', '0004_auto_20150421_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='company',
            field=models.CharField(default='Langoor', max_length=200),
            preserve_default=False,
        ),
    ]
