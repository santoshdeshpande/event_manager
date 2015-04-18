# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_time', models.CharField(max_length=100, null=True, blank=True)),
                ('session_info', models.TextField(null=True, blank=True)),
                ('order', models.IntegerField()),
                ('session_type', models.CharField(max_length=20, choices=[(b'break', b'Break'), (b'header', b'Header'), (b'session', b'Session')])),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact', models.TextField()),
                ('office_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('table_name', models.CharField(max_length=100)),
                ('topic', models.TextField()),
                ('meeting_of', models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('meeting_with', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=500)),
                ('option1', models.CharField(max_length=50)),
                ('option2', models.CharField(max_length=50)),
                ('option3', models.CharField(max_length=50)),
                ('option4', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='SurveyAnswers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('answer1', models.CharField(max_length=50, null=True, blank=True)),
                ('answer2', models.CharField(max_length=50, null=True, blank=True)),
                ('answer3', models.CharField(max_length=50, null=True, blank=True)),
                ('answer4', models.CharField(max_length=50, null=True, blank=True)),
                ('answer5', models.CharField(max_length=50, null=True, blank=True)),
                ('answer6', models.CharField(max_length=50, null=True, blank=True)),
                ('answer7', models.CharField(max_length=50, null=True, blank=True)),
                ('answer8', models.CharField(max_length=50, null=True, blank=True)),
                ('answer9', models.CharField(max_length=50, null=True, blank=True)),
                ('answer10', models.CharField(max_length=50, null=True, blank=True)),
                ('answer11', models.CharField(max_length=50, null=True, blank=True)),
                ('answer12', models.CharField(max_length=50, null=True, blank=True)),
                ('answer13', models.CharField(max_length=50, null=True, blank=True)),
                ('answer14', models.CharField(max_length=50, null=True, blank=True)),
                ('answer15', models.CharField(max_length=50, null=True, blank=True)),
                ('answer16', models.CharField(max_length=50, null=True, blank=True)),
                ('answer17', models.CharField(max_length=50, null=True, blank=True)),
                ('answer18', models.CharField(max_length=50, null=True, blank=True)),
                ('answer19', models.CharField(max_length=50, null=True, blank=True)),
                ('answer20', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=200)),
                ('profile', models.TextField()),
                ('userType', models.CharField(default=b'speaker', max_length=20, choices=[(b'wipro', b'Wipro Leader'), (b'speaker', b'Speaker'), (b'participant', b'Participant')])),
                ('has_profile_info', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to=b'profiles')),
            ],
        ),
    ]
