from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Agenda(models.Model):
	CHOICES = (
		('break', 'Break'),
		('header', 'Header'),
		('session', 'Session')
	)
	session_time = models.CharField(max_length = 100, null=True,blank=True)
	session_info = models.TextField(null=True,blank=True)
	order = models.IntegerField()
	session_type = models.CharField(max_length=20,choices=CHOICES)

	class Meta:
		ordering = ('order',)

class UserProfile(models.Model):
	CHOICES = (
		('wipro', 'Wipro Leader'),
		('speaker', 'Speaker'),
		('participant', 'Participant')
	)
	name = models.CharField(max_length = 255)
	title = models.CharField(max_length = 200)
	profile = models.TextField(blank=True,null=True)
	userType = models.CharField(max_length = 20, choices = CHOICES, default='speaker')
	has_profile_info = models.BooleanField(default=True)
	image = models.ImageField(upload_to="profiles", blank=True, null=True)

	@property
	def starting_field(self):
		return self.name[0];

class ContactInfo(models.Model):
	contact = models.TextField();
	office_address = models.TextField();

	class Meta:
		verbose_name = 'Contact Information'
		verbose_name_plural = 'Contact Information'

class Survey(models.Model):
	question = models.CharField(max_length = 500)
	option1 = models.CharField(max_length = 50)
	option2 = models.CharField(max_length = 50)
	option3 = models.CharField(max_length = 50)
	option4 = models.CharField(max_length = 50)

	class Meta:
		ordering = ('id',)

class SurveyAnswers(models.Model):
	email = models.CharField(max_length = 100)
	name = models.CharField(max_length = 100)
	answer1 = models.CharField(max_length=50, null=True,blank=True)
	answer2 = models.CharField(max_length=50, null=True,blank=True)
	answer3 = models.CharField(max_length=50, null=True,blank=True)
	answer4 = models.CharField(max_length=50, null=True,blank=True)
	answer5 = models.CharField(max_length=50, null=True,blank=True)
	answer6 = models.CharField(max_length=50, null=True,blank=True)
	answer7 = models.CharField(max_length=50, null=True,blank=True)
	answer8 = models.CharField(max_length=50, null=True,blank=True)
	answer9 = models.CharField(max_length=50, null=True,blank=True)
	answer10 = models.CharField(max_length=50, null=True,blank=True)
	answer11 = models.CharField(max_length=50, null=True,blank=True)
	answer12 = models.CharField(max_length=50, null=True,blank=True)
	answer13 = models.CharField(max_length=50, null=True,blank=True)
	answer14 = models.CharField(max_length=50, null=True,blank=True)
	answer15 = models.CharField(max_length=50, null=True,blank=True)
	answer16 = models.CharField(max_length=50, null=True,blank=True)
	answer17 = models.CharField(max_length=50, null=True,blank=True)
	answer18 = models.CharField(max_length=50, null=True,blank=True)
	answer19 = models.CharField(max_length=50, null=True,blank=True)
	answer20 = models.CharField(max_length=50, null=True,blank=True)

	class Meta:
		verbose_name = 'Survey Answer'
		verbose_name_plural = 'Survey Answers'

class UserMeeting(models.Model):
	meeting_of = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='host',verbose_name = 'Wipro Leader')
	meeting_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attendee', verbose_name='Analyst')
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	venue = models.CharField(max_length = 100)		
	topic = models.TextField()
	modified = models.DateTimeField(auto_now=True)
		
	@property
	def start_time_str(self):
		return self.start_time.strftime("%I:%M %p")

	@property
	def end_time_str(self):
		return self.end_time.strftime("%I:%M %p")

	@property
	def wipro_leaders(self):    
		return "\n".join([p.get_full_name() for p in self.meeting_with.all()])		

	@property
	def analysts(self):    
		return "\n".join([p.get_full_name() for p in self.meeting_of.all()])		


	class Meta:
		ordering = ('start_time','modified',)


class Meeting(models.Model):
	meeting_of = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner')
	meeting_with = models.ForeignKey(settings.AUTH_USER_MODEL)	
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	table_name = models.CharField(max_length = 100)
	topic = models.TextField()
	modified = models.DateTimeField(auto_now=True)
	approved = models.BooleanField(default=True)

	@property
	def meeting_with_name(self):
		return self.meeting_with.first_name + " " + self.meeting_with.last_name;

	@property
	def start_time_str(self):
		return self.start_time.strftime("%I:%M %p")

	@property
	def end_time_str(self):
		return self.end_time.strftime("%I:%M %p")

	class Meta:
		ordering = ('start_time','modified',)

class MeetingRequest(models.Model):
	name = models.CharField(max_length = 100)
	company = models.CharField(max_length = 100)
	designation = models.CharField(max_length = 100)
	wiproLeader = models.CharField(max_length = 100)
	comments = models.TextField();

class Feedback(models.Model):
	email = models.CharField(max_length = 100);
	name = models.CharField(max_length = 200);
	question1 = models.TextField();
	question2 = models.TextField();
	question3 = models.TextField();
	question4 = models.TextField();
	question5 = models.TextField();

class Chat(models.Model):
	email = models.CharField(max_length = 100);
	name = models.CharField(max_length = 200);
	message = models.TextField();
	modified = models.DateTimeField(auto_now=True);

	class Meta:
		ordering = ('-modified',)	
		verbose_name = 'Chat Message'
		verbose_name_plural = 'Chat Messages'


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
	CHOICES = (
		('wipro', 'Wipro Leader'),
		('speaker', 'Speaker'),
		('participant', 'Participant')
	)	
	email = models.EmailField('email address', unique=True, db_index=True)
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	company = models.CharField(max_length = 200)
	title = models.CharField(max_length = 200,blank=True,null=True)
	profile = models.TextField(blank=True,null=True)
	userType = models.CharField(max_length = 20, choices = CHOICES, default='speaker')
	has_profile_info = models.BooleanField(default=True)
	image = models.ImageField(upload_to="profiles", blank=True, null=True)
	date_joined = models.DateTimeField(auto_now_add=True)	
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)		

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	objects = CustomUserManager()

	def get_short_name(self):
		return self.first_name

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	@property
	def starting_field(self):
		full_name = self.get_full_name();
		start = self.email[0]
		if(full_name != ""):
			start = self.get_full_name()[0]
		return start.upper()
		



	def __unicode__(self):
		return "%s (%s)"% (self.get_full_name(), self.email)









	

