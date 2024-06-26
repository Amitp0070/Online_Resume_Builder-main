from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name = 'resume'),
    path("resumetemplate", views.resumetemplate, name="resumetemplate"),
    path("resume_templates", views.resume_templates, name="resume_templates"),
    path("resumetemplatedownload", views.resumetemplatedownload, name="resumetemplatedownload"),
    path('tryforfree/', views.tryforfree, name='tryforfree'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)