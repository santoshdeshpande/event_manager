from rest_framework import serializers
from .models import ContactInfo, UserProfile,Agenda,Survey,SurveyAnswers,Meeting,MeetingRequest,Feedback,Chat,CustomUser,UserMeeting
from django.contrib.auth.models import User
from django.conf import settings



class UserProfileSerializer(serializers.ModelSerializer):
	start = serializers.CharField(source='starting_field')
	image_url = serializers.SerializerMethodField()

	def get_image_url(self, obj):
		return '%s%s' % (settings.MEDIA_URL, obj.image)

	class Meta:
		model = CustomUser

class ContactInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContactInfo	

class AgendaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Agenda

class SurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = Survey

class SurveyAnswersSerializer(serializers.ModelSerializer):
	class Meta:
		model = SurveyAnswers

class UserSerializer(serializers.ModelSerializer):
	start = serializers.CharField(source='starting_field')
	image_url = serializers.SerializerMethodField()
	name = serializers.SerializerMethodField()

	def get_name(self, obj):
		return "%s %s" % (obj.first_name, obj.last_name)

	def get_image_url(self, obj):
		return '%s%s' % (settings.MEDIA_URL, obj.image)

	class Meta:
		model = CustomUser
		fields = ('id','name','first_name','last_name','email','title','image','profile','userType','company','start','image_url')

class MeetingSerializer(serializers.ModelSerializer):
	meeting_of = UserSerializer(read_only=True)
	meeting_with = UserSerializer(read_only=True)
	meeting_with_name = serializers.CharField()
	start_time_str = serializers.CharField()
	end_time_str = serializers.CharField()
	class Meta:
		model = Meeting

class UserMeetingSerializer(serializers.ModelSerializer):
	meeting_of = UserSerializer(read_only=True, many=True)
	meeting_with = UserSerializer(read_only=True, many=True)
	start_time_str = serializers.CharField()
	end_time_str = serializers.CharField()

	class Meta:
		model = UserMeeting

class MeetingRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = MeetingRequest

class FeedbackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Feedback

class ChatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chat
