from django import forms
from .models import CVRequest

class CreateYoursForm(forms.ModelForm):
    class Meta:
        model = CVRequest
        fields = ['photo', 'description', 'role', 'linkedin', 'github', 'instagram', 
                  'project_title_1', 'project_description_1', 'project_title_2', 
                  'project_description_2', 'project_title_3', 'project_description_3', 
                  'experience']
