from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^post/',views.post, name='post'),
    url('^api/project/$', views.ProjectList.as_view()),
    url('^api/profile/$', views.ProfileList.as_view()),
    url("^profile/", views.profile, name="profile"),
    url('^update_profile/$',views.update_profile,name = 'update_profile'),
    url('^project/(\d+)', views.project, name='project'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)