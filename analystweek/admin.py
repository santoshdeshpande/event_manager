from django.contrib import admin
from .models import UserProfile,ContactInfo,Agenda,Survey,SurveyAnswers,Meeting,Feedback,Chat,CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
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

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name','last_name','company')}),
        (_('Analyst info'), {'fields':('title','userType','profile','has_profile_info','image')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)



admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Survey,SurveyAdmin)
admin.site.register(SurveyAnswers,SurveyAnswersAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Chat,ChatAdmin)
admin.site.register(CustomUser,CustomUserAdmin)