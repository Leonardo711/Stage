"""Stage URL Configuration

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
    u
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^getContent', getContent),
    url(r'^$',index),
    url(r'^language/', language),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^team/', include('team.urls')),
    url(r'^notice/', include('notice.urls')),
    url(r'^accounts/', include('userClass.urls')),
    url(r'^project/', include('project.urls')),
    url(r'^team/', include('team.urls')),
    url(r'^article/', include('article.urls')),
    url(r'^academic/', include('academic.urls')),
    url(r'^tools/', include("tools.urls")),
    url(r'^progress/', include("progress.urls")),
    url(r'^i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
