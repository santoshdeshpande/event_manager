# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analystweek', '0003_auto_20150418_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('wiproLeader', models.CharField(max_length=100)),
                ('comments', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='meeting',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
