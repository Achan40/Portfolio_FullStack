from django import forms
from Basic_app.models import Project,Contact
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta():
        model = Contact
        fields = ('author','email','text')

class ProjectForm(forms.ModelForm):
    class Meta():
        model = Project
        fields = ('rank','project_pic','author','link','title','summary','text')