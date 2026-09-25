from django.db import models


class Citizen(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)

    # Contact Information
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    # Address Information
    address = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default="Maharashtra")
    pincode = models.CharField(max_length=10)

    # Government Identification
    aadhaar_number = models.CharField(max_length=12, unique=True)

    # Service Information
    service_type = models.CharField(max_length=100)

    # Status
    status = models.CharField(
        max_length=30,
        default="Pending"
    )

    # Registration Date
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


from django.db import models

# Create your models here.
