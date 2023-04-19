"""db_project URL Configuration

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
from django.urls import re_path, include
from django.contrib import admin
from base_app import views

urlpatterns = [
    re_path(r'^available/', views.available_books, name='available'),
    re_path(r'^home/', views.home, name='home'),
    re_path(r'^catalogue/', views.catalogue, name='catalogue'),
    re_path(r'^profile/', views.profile, name='profile'),
    re_path(r'^checkout/(?P<book_id>[0-9]+)/$', views.checkout_book, name='checkout'),
    re_path(r'^checkin/(?P<circulation_id>[0-9]+)/$', views.checkin_book, name='checkin'),
]
