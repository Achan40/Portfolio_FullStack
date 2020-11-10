from django.db import models
from django.urls import reverse
from django.utils import timezone

# Model for various projects
class Project(models.Model):

    # Only expecting one user, as this is a personal porfolio
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    
    rank = models.IntegerField()
    project_pic = models.ImageField(upload_to='project_pic', blank=True)
    link = models.URLField()
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=500)
    text = models.TextField()

    def __str__(self):
        return self.title

    # After a new project is created, go to its detail page
    def get_absolute_url(self):
        return reverse('project_detail',kwargs={'pk':self.pk})

# Model for contact form
class Contact(models.Model):
    author = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    text = models.TextField(max_length=1000)
    contact_date = models.DateTimeField(default=timezone.now)

    # After a contact is created, go to the about page
    def get_absolute_url(self):
        return reverse('contact_confirm')