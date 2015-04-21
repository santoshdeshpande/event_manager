# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name=b'email address', db_index=True)),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=200)),
                ('profile', models.TextField(null=True, blank=True)),
                ('userType', models.CharField(default=b'speaker', max_length=20, choices=[(b'wipro', b'Wipro Leader'), (b'speaker', b'Speaker'), (b'participant', b'Participant')])),
                ('has_profile_info', models.BooleanField(default=True)),
                ('image', models.ImageField(null=True, upload_to=b'profiles', blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
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
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-modified',),
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
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('table_name', models.CharField(max_length=100)),
                ('topic', models.TextField()),
                ('modified', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=True)),
                ('meeting_of', models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('meeting_with', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('start_time', 'modified'),
            },
        ),
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
                ('profile', models.TextField(null=True, blank=True)),
                ('userType', models.CharField(default=b'speaker', max_length=20, choices=[(b'wipro', b'Wipro Leader'), (b'speaker', b'Speaker'), (b'participant', b'Participant')])),
                ('has_profile_info', models.BooleanField(default=True)),
                ('image', models.ImageField(null=True, upload_to=b'profiles', blank=True)),
            ],
        ),
    ]
