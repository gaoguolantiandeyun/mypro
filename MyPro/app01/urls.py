from django.contrib import admin
from django.urls import path
from app01 import views
from django.conf.urls import url, include

urlpatterns = [
    path('login/', views.login, name="denglu"),
    path('auth/', views.auth, name="renzheng"),
    path('index/', views.index, name="zhuye"),
    path("test/", views.test),
    url(r"articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$",views.days),
]