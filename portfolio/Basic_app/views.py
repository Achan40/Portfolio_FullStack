from django.shortcuts import render
from Basic_app.models import Project,Contact # models
from Basic_app.forms import ContactForm,ProjectForm
from django.views.generic import TemplateView,CreateView,ListView,DetailView

# View for the about page
class AboutView(TemplateView):
    template_name = 'about.html'

# View for Contact page
class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    model = Contact

class ContactConfirmed(TemplateView):
    template_name = 'contact_confirm.html'

# View for list of projects
class ProjectList(ListView):
    template_name = 'projects.html'
    model = Project
# Add functionality later to filter by condition. (def get_queryset)

# View for New Project Create page
class ProjectCreate(CreateView):
    template_name = 'project_form.html'
    form_class = ProjectForm
    model = Project

# Detail View for Projects
class ProjectDetailView(DetailView):
    model = Project