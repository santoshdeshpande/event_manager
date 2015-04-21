# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analystweek', '0005_auto_20150420_0218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('question1', models.TextField()),
                ('question2', models.TextField()),
                ('question3', models.TextField()),
                ('question4', models.TextField()),
                ('question5', models.TextField()),
            ],
        ),
    ]
