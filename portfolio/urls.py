"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url,include
from django.contrib.auth import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',include('Basic_app.urls')),

    # adding login and logout functionality
    # django automatically links up the view of this page with login.html since it is in templates directory
    url(r'^accounts/login/$',views.LoginView.as_view(),name='login'),

    # When you logout, you return to the about page
    url(r'^accounts/logout/$',views.LogoutView.as_view(next_page='about'),name='logout'),

    #add captcha
    path('captcha/',include('captcha.urls'))

] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)