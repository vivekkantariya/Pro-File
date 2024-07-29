from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projectView, name='projects'),
    path('experience/', views.experienceView, name='experience'),
    path('contact/', views.contactView, name='contact'),    
    path('createyours/', views.createYoursView, name='createyours'),    
    path('create-yours/', views.create_yours, name='create_yours'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)