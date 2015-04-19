from django.shortcuts import render

from .models import ContactInfo,UserProfile,Agenda,Survey,SurveyAnswers,Meeting,MeetingRequest
from .serializers import ContactInfoSerializer, UserProfileSerializer,AgendaSerializer,SurveySerializer,UserSerializer,SurveyAnswersSerializer,MeetingSerializer,MeetingRequestSerializer

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
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
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
	serializer_class = MeetingSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		user = self.request.user
		return Meeting.objects.filter(meeting_of=user).filter(approved=True)


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

# Create your views here.
