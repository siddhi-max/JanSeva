from django import forms
from .models import Citizen


class CitizenForm(forms.ModelForm):

    class Meta:
        model = Citizen

        fields = [
            'full_name',
            'date_of_birth',
            'gender',
            'mobile_number',
            'email',
            'address',
            'city',
            'district',
            'state',
            'pincode',
            'aadhaar_number',
            'service_type',
            'status',
        ]

        widgets = {

            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }),

            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'gender': forms.Select(
                choices=[
                    ('', 'Select Gender'),
                    ('Male', 'Male'),
                    ('Female', 'Female'),
                    ('Other', 'Other'),
                ],
                attrs={
                    'class': 'form-control'
                }
            ),

            'mobile_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter mobile number'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter complete address',
                'rows': 4
            }),

            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter city'
            }),

            'district': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter district'
            }),

            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter state'
            }),

            'pincode': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter pincode'
            }),

            'aadhaar_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Aadhaar number'
            }),

            'service_type': forms.Select(
                choices=[
                    ('', 'Select Service'),
                    ('Income Certificate', 'Income Certificate'),
                    ('Caste Certificate', 'Caste Certificate'),
                    ('Domicile Certificate', 'Domicile Certificate'),
                    ('Birth Certificate', 'Birth Certificate'),
                    ('Death Certificate', 'Death Certificate'),
                    ('Other', 'Other'),
                ],
                attrs={
                    'class': 'form-control'
                }
            ),

            'status': forms.Select(
                choices=[
                    ('Pending', 'Pending'),
                    ('Processing', 'Processing'),
                    ('Approved', 'Approved'),
                    ('Rejected', 'Rejected'),
                    ('Completed', 'Completed'),
                ],
                attrs={
                    'class': 'form-control'
                }
            ),
        }