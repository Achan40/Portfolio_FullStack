from django.shortcuts import render
from Basic_app.models import Project,Contact # models
from Basic_app.forms import ContactForm,ProjectForm
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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

# Detail View for Projects
class ProjectDetailView(DetailView):
    model = Project

# View for New Project Create page, requires a login first
class ProjectCreate(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'project/project_detail.html'
    template_name = 'project_form.html'
    form_class = ProjectForm
    model = Project

# View for project update
class ProjectUpdate(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'project/project_detail.html'
    form_class = ProjectForm
    model = Project

# View for project delete
class ProjectDelete(LoginRequiredMixin,DeleteView):
    template_name = 'project_delete_confirm.html'
    model = Project
    success_url = reverse_lazy('project_list')


