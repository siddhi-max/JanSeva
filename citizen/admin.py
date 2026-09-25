
from django.contrib import admin
from .models import Citizen


@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'mobile_number',
        'city',
        'district',
        'service_type',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'service_type',
        'gender',
        'district',
    )

    search_fields = (
        'full_name',
        'mobile_number',
        'aadhaar_number',
        'city',
        'district',
    )

    ordering = (
        '-created_at',
    )