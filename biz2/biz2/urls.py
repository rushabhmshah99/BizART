"""biz2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/', 'polls.views.addition'),
    url(r'^index/', 'themeSetup.views.index'),
    url(r'^aboutus/', 'themeSetup.views.aboutus'),
    url(r'^login_simple/', 'themeSetup.views.login_simple'),
    url(r'^login_advanced/(?P<username>[a-z]+)', 'themeSetup.views.login_advanced'),
     url(r'^login_advanced/', 'themeSetup.views.login_advanced'),
    url(r'^search/', 'themeSetup.views.search'),
       
 

] 
