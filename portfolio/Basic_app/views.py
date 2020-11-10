from django.shortcuts import render,redirect
from Basic_app.models import Project,Contact # models
from Basic_app.forms import ContactForm,ProjectForm
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# View for the about page
class AboutView(TemplateView):
    template_name = 'about.html'

# View for Contact page with captcha
def Contact_View(request):

    if request.method == 'POST':
        contact = ContactForm(request.POST)

        # Validate form and check input
        if contact.is_valid():
            contact.save()
            return redirect('contact_confirm')
    else:
        contact = ContactForm()

    return render(request, 'contact.html', {'contact':contact})

# Contact confirmation page
class ContactConfirmed(TemplateView):
    template_name = 'contact_confirm.html'

# View for list of projects
class ProjectList(ListView):
    template_name = 'project_list.html'
    model = Project

    # order by rank ascending
    def get_queryset(self):
        return Project.objects.all().order_by('rank')


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


