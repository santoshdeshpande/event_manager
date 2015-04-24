# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analystweek', '0009_customuser_show_in_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer10',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer11',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer12',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer13',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer14',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer15',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer16',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer17',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer18',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer19',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer20',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer3',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer4',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer5',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer6',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer7',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer8',
        ),
        migrations.RemoveField(
            model_name='surveyanswers',
            name='answer9',
        ),
        migrations.AlterField(
            model_name='surveyanswers',
            name='answer1',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
