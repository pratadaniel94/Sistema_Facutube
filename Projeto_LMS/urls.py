"""Projeto_LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from core.views import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^index', index),
    url(r'^contato', contato),
    url(r'^noticia', noticia),
    url(r'^curso', cursos),
    url(r'^marketing', marketing),
    url(r'^blogger',blogger ),
    url(r'^desing',desing ),
    url(r'^publicidade',publicidade ),
    url(r'^esqueci-senha',esqueci ),
    url(r"^login/", login, {"template_name": "login.html"}),
    url(r"^sair/", logout, {'next_page': 'index'}),
    
]
