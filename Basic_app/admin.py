from django.contrib import admin
from Basic_app.models import Project,Contact

# Register models so that we can see them on the admin site
admin.site.register(Project)
admin.site.register(Contact)