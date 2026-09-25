from django.urls import path
from . import views


urlpatterns = [

    # Citizen Registration
    path(
        'register/',
        views.citizen_register,
        name='citizen_register'
    ),

    # Registration Success
    path(
        'success/',
        views.citizen_success,
        name='citizen_success'
    ),

    # Citizen List + Search
    path(
        'list/',
        views.citizen_list,
        name='citizen_list'
    ),

    # Citizen Details
    path(
        'detail/<int:citizen_id>/',
        views.citizen_detail,
        name='citizen_detail'
    ),

    # Edit Citizen
    path(
        'edit/<int:citizen_id>/',
        views.citizen_edit,
        name='citizen_edit'
    ),

    # Delete Citizen
    path(
        'delete/<int:citizen_id>/',
        views.citizen_delete,
        name='citizen_delete'
    ),

]