from rest_framework import serializers
from .models import ContactInfo, UserProfile,Agenda,Survey,SurveyAnswers,Meeting,MeetingRequest,Feedback
from django.contrib.auth.models import User
from django.conf import settings

class UserProfileSerializer(serializers.ModelSerializer):
	start = serializers.CharField(source='starting_field')
	image_url = serializers.SerializerMethodField()

	def get_image_url(self, obj):
		return '%s%s' % (settings.MEDIA_URL, obj.image)

	class Meta:
		model = UserProfile

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
	class Meta:
		model = User
		fields = ('id','first_name','last_name','email',)

class MeetingSerializer(serializers.ModelSerializer):
	meeting_of = UserSerializer(read_only=True)
	meeting_with = UserSerializer(read_only=True)
	meeting_with_name = serializers.CharField()
	start_time_str = serializers.CharField()
	end_time_str = serializers.CharField()
	class Meta:
		model = Meeting

class MeetingRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = MeetingRequest

class FeedbackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Feedback

