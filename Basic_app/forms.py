from django import forms
from Basic_app.models import Project,Contact
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta():
        model = Contact
        fields = ('author','email','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'form-control','id':'contact_author','placeholder':'Enter your name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':'contact_email','placeholder':'Enter your email'}),
            'text':forms.Textarea(attrs={'class':'form-control','id':'contact_text','placeholder':'Enter a message'}),
        }
    

class ProjectForm(forms.ModelForm):
    class Meta():
        model = Project
        fields = ('rank','project_pic','author','link','title','summary','text')

        widgets = {
            'rank':forms.NumberInput(attrs={'class':'form-control','placeholder':'Select Ranking'}),
            'project_pic':forms.ClearableFileInput(attrs={'type':'file','class':'form-control-file'}),            
            'author':forms.Select(attrs={'class':'form-control','placeholder':'Enter your name'}),
            'link':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a link'}),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a title'}),            
            'summary':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter a summary','rows':'3'}),
            'text':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter a long description'}),
        }