from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projectView, name='projects'),
    path('experience/', views.experienceView, name='experience'),
    path('contact/', views.contactView, name='contact'),    
    path('createyours/', views.createYoursView, name='createyours'),    
    path('create-yours/', views.create_yours, name='create_yours'),

]