"""songs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from song.views import filterq,playlist_v,playlist_d,index,filteralbum,filterartist,main_site,main_page
from django.conf.urls.static import static
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^genre/',filterq),
    url(r'^songs/',main_page,name='song'),
    url(r'^artist/',filterartist),
    url(r'^album/',filteralbum),
    url(r'^index/',index),
    url(r'^playlist/',playlist_v),
    url(r'^playlistd/',playlist_d),
    url(r'^home/',TemplateView.as_view(template_name='song/details.html'), name='home page'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
                               
                               
                              
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

