from django.db import models

class CVRequest(models.Model):
    photo = models.ImageField(upload_to='photos/')
    description = models.TextField()
    role = models.CharField(max_length=100)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    
    project_title_1 = models.CharField(max_length=200)
    project_description_1 = models.TextField()
    project_title_2 = models.CharField(max_length=200, blank=True, null=True)
    project_description_2 = models.TextField(blank=True, null=True)
    project_title_3 = models.CharField(max_length=200, blank=True, null=True)
    project_description_3 = models.TextField(blank=True, null=True)
    
    experience = models.TextField()
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='pending')

    def __str__(self):
        return f"{self.role} - {self.status}"
