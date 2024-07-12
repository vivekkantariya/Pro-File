from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'resume/home.html')

def projectView(request):
    return render(request, 'resume/projects.html')

def experienceView(request):
    return render(request, 'resume/experience.html')

def contactView(request):
    return render(request, 'resume/contact.html')