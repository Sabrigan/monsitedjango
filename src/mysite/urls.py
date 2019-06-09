"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import re_path, url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

handler404 = 'mysite.views.handler404'
handler500 = 'mysite.views.handler500'


urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path('^about/', views.about, name='about'),
    re_path('^contact/', views.contact, name='contact'),
    url(r'^blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Sabrigan Admin"
admin.site.site_title = "Portail Administration Sabrigan"
admin.site.index_title = "Bienvenue sur le site admin de MR Sabrigan"
