from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateYoursForm
# Create your views here.

def home(request):
    return render(request, 'resume/home.html')

def projectView(request):
    return render(request, 'resume/projects.html')

def experienceView(request):
    return render(request, 'resume/experience.html')

def contactView(request):
    return render(request, 'resume/contact.html')

def createYoursView(request):
    return render(request, 'resume/createyours.html')

def create_yours(request):
    if request.method == 'POST':
        form = CreateYoursForm(request.POST, request.FILES)
        if form.is_valid():
            # Process form data here
            # Save data to the database, create CV, etc.
            return HttpResponse("Your CV has been created successfully!")
    else:
        form = CreateYoursForm()

    return render(request, 'createyours.html', {'form': form})