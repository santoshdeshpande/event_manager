from django.shortcuts import render

from .models import ContactInfo,UserProfile,Agenda,Survey,SurveyAnswers,Meeting,MeetingRequest,Feedback,Chat,CustomUser,UserMeeting
from .serializers import ContactInfoSerializer, UserProfileSerializer,AgendaSerializer,SurveySerializer,UserSerializer,SurveyAnswersSerializer,MeetingSerializer,MeetingRequestSerializer,FeedbackSerializer,ChatSerializer,UserMeetingSerializer

from rest_framework import permissions

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response

class ContactInfoList(generics.ListCreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


    def get(self, request, *args, **kwargs):
    	print request.user
    	return self.list(request, *args, **kwargs)


    def perform_create(self, serializer):
    	print "Performing create..."

class UserProfileList(generics.ListAPIView):	
	queryset = CustomUser.objects.filter(is_staff=False)
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticated,)

class AgendaList(generics.ListAPIView):	
	queryset = Agenda.objects.all()
	serializer_class = AgendaSerializer
	permission_classes = (permissions.IsAuthenticated,)

class SurveyAnswersList(generics.ListCreateAPIView):
	queryset = SurveyAnswers.objects.all()
	serializer_class = SurveyAnswersSerializer
	permission_classes = (permissions.IsAuthenticated,)



class SurveyList(generics.ListAPIView):	
	queryset = Survey.objects.all()
	serializer_class = SurveySerializer
	permission_classes = (permissions.IsAuthenticated,)

class MeetingList(generics.ListCreateAPIView):		
	serializer_class = UserMeetingSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		user = self.request.user
		host = user.host.all()
		attendee = user.attendee.all()
		all_meetings = []
		all_meetings.append(host)
		all_meetings.append(attendee)
		meetings = [item for sublist in all_meetings for item in sublist]
		return meetings


class MeetingRequestList(generics.ListCreateAPIView):
	queryset = MeetingRequest.objects.all()
	serializer_class = MeetingRequestSerializer
	permission_classes = (permissions.IsAuthenticated,)


class UserInfo(generics.RetrieveAPIView):
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def retrieve(self, request, *args, **kwargs):
		instance = request.user
		serializer = self.get_serializer(instance)
		return Response(serializer.data)

class FeedbackInfo(generics.ListCreateAPIView):
	queryset = Feedback.objects.all();
	serializer_class = FeedbackSerializer
	permission_classes = (permissions.IsAuthenticated,)

class ChatList(generics.ListCreateAPIView):
	queryset = Chat.objects.all();
	serializer_class = ChatSerializer
	permission_classes = (permissions.IsAuthenticated,)



# Create your views here.
