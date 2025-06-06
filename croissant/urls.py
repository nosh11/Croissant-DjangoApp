"""
URL configuration for croissant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from croissant import settings, views

from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('novel/', include('novel.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('boy/', include('boy.urls')),
    path('',  views.root),
]


# MEDIA_ROOTを公開する(アクセス可能にする)　
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

# DEBUG=FalseでもMEDIA_ROOTを見える様にする
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]