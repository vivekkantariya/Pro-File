from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import CreateYoursForm
from .models import CVRequest

def create_yours(request):
    if request.method == 'POST':
        form = CreateYoursForm(request.POST, request.FILES)
        if form.is_valid():
            cv_request = form.save()
            
            # Process form data and send email
            subject = 'New CV Creation Request'
            message = f"""
            Description: {cv_request.description}
            Role: {cv_request.role}
            LinkedIn: {cv_request.linkedin}
            GitHub: {cv_request.github}
            Instagram: {cv_request.instagram}
            Experience: {cv_request.experience}
            Project 1: {cv_request.project_title_1} - {cv_request.project_description_1}
            Project 2: {cv_request.project_title_2} - {cv_request.project_description_2}
            Project 3: {cv_request.project_title_3} - {cv_request.project_description_3}
            """
            accept_url = request.build_absolute_uri(f"/accept/{cv_request.id}/")
            decline_url = request.build_absolute_uri(f"/decline/{cv_request.id}/")
            message += f"\nAccept: {accept_url}\nDecline: {decline_url}"

            # Send email
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])

            return redirect('thank_you')
    else:
        form = CreateYoursForm()

    return render(request, 'createyours.html', {'form': form})

def accept_request(request, request_id):
    cv_request = get_object_or_404(CVRequest, id=request_id)
    cv_request.status = 'accepted'
    cv_request.save()
    # Generate CV
    return HttpResponse('CV request accepted and generated.')

def decline_request(request, request_id):
    cv_request = get_object_or_404(CVRequest, id=request_id)
    cv_request.status = 'declined'
    cv_request.save()
    return HttpResponse('CV request declined.')

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

