from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [

    # Admin
    path(
        'admin/',
        admin.site.urls
    ),

    # Dashboard
    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    # Reports
    path(
        'reports/',
        views.reports,
        name='reports'
    ),

    # Citizen
    path(
        'citizen/',
        include('citizen.urls')
    ),

]