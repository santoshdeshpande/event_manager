from django.conf.urls import include, url, patterns
from django.contrib import admin
from analystweek import views
from django.conf import settings;

urlpatterns = [
    # Examples:
    # url(r'^$', 'event_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/v1/contact_info/$', views.ContactInfoList.as_view()),
    url(r'^api/v1/user_profiles/$', views.UserProfileList.as_view()),
    url(r'^api/v1/agenda/$', views.AgendaList.as_view()),
    url(r'^api/v1/user/$', views.UserInfo.as_view()),
    url(r'^api/v1/survey/$', views.SurveyList.as_view()),
    url(r'^api/v1/survey_answers/$', views.SurveyAnswersList.as_view()),
    url(r'^api/v1/meetings/$', views.MeetingList.as_view()),
    url(r'^api/v1/request_meeting/$', views.MeetingRequestList.as_view()),
    url(r'^api/v1/feedback/$', views.FeedbackInfo.as_view()),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.MEDIA_ROOT}))
