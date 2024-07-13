from django import forms

class CreateYoursForm(forms.Form):
    photo = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea)
    role = forms.CharField(max_length=100)
    linkedin = forms.URLField(required=False)
    instagram = forms.URLField(required=False)
    github = forms.URLField(required=False)
    project1 = forms.CharField(max_length=200)
    project2 = forms.CharField(max_length=200)
    project3 = forms.CharField(max_length=200)
    experience = forms.CharField(widget=forms.Textarea)
