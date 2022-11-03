from django import forms
from app.models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        exclude = ['skill', 'author', 'slug']
        
