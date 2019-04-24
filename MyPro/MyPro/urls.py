"""MyPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app01 import views
from django.conf.urls import url,include



urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('login.html/', views.login,name="denglu"),
    # path('auth/', views.auth),
    # path('index/', views.index),
    # ---------------------------------
    # url(r"^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$",views.days),
    # url(r"^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$",views.days2),
    url(r"app01/",include("app01.urls")),
    url(r"app02/",include("app02.urls")),


]
