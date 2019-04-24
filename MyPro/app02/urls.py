from django.contrib import admin
from django.urls import path
from app02 import views
from django.conf.urls import url,include



urlpatterns = [
   path("product/",views.every_prod),
   path("bianliang/",views.show_time),
   path("guolvqi/",views.show_guolv),
]