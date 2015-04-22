# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('analystweek', '0005_customuser_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMeeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('venue', models.CharField(max_length=100)),
                ('topic', models.TextField()),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('start_time', 'modified'),
            },
        ),
        migrations.AlterModelOptions(
            name='chat',
            options={'ordering': ('-modified',), 'verbose_name': 'Chat Message', 'verbose_name_plural': 'Chat Messages'},
        ),
        migrations.AlterModelOptions(
            name='contactinfo',
            options={'verbose_name': 'Contact Information', 'verbose_name_plural': 'Contact Information'},
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='surveyanswers',
            options={'verbose_name': 'Survey Answer', 'verbose_name_plural': 'Survey Answers'},
        ),
        migrations.AddField(
            model_name='usermeeting',
            name='meeting_of',
            field=models.ManyToManyField(related_name='m_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usermeeting',
            name='meeting_with',
            field=models.ManyToManyField(related_name='m_others', to=settings.AUTH_USER_MODEL),
        ),
    ]
