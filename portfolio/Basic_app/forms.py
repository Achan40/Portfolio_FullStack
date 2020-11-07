from django import forms
from Basic_app.models import Project,Contact

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = ('author','email','text')

class ProjectForm(forms.ModelForm):
    class Meta():
        model = Project
        fields = ('project_pic','author','link','title','summary','text')