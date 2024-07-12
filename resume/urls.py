from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projectView, name='projects'),
    path('experience/', views.experienceView, name='experience'),
    path('contact/', views.contactView, name='contact'),    
]