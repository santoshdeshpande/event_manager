from django.db import models
from django.contrib.auth.models import User

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

class Meeting(models.Model):
	meeting_of = models.ForeignKey('auth.User', related_name='owner')
	meeting_with = models.ForeignKey('auth.User')	
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
		ordering = ('modified',)	







	

