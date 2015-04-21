from django.contrib import admin
from .models import UserProfile,ContactInfo,Agenda,Survey,SurveyAnswers,Meeting,Feedback,Chat

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('name','title','userType','has_profile_info')
	list_filter = ('userType', 'has_profile_info')
	
class ContactInfoAdmin(admin.ModelAdmin):
	list_display = ('contact','office_address')

class AgendaAdmin(admin.ModelAdmin):
	list_display = ('order','session_time','session_info','session_type')

class SurveyAdmin(admin.ModelAdmin):
	list_display = ('question','option1','option2','option3','option4')

class SurveyAnswersAdmin(admin.ModelAdmin):
	list_display = ('email','name')

class MeetingAdmin(admin.ModelAdmin):
	list_display = ('meeting_with_name','table_name','topic','start_time_str','end_time_str')

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('name','email','question1','question2','question3','question4','question5')


class ChatAdmin(admin.ModelAdmin):
	list_display = ('name','email','message','modified')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Survey,SurveyAdmin)
admin.site.register(SurveyAnswers,SurveyAnswersAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Chat,ChatAdmin)