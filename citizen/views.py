from django.shortcuts import render, redirect, get_object_or_404

from .forms import CitizenForm
from .models import Citizen


# ==============================
# Citizen Registration
# ==============================

def citizen_register(request):

    if request.method == 'POST':

        form = CitizenForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('citizen_success')

    else:

        form = CitizenForm()

    return render(
        request,
        'citizen/register.html',
        {
            'form': form
        }
    )


# ==============================
# Registration Success
# ==============================

def citizen_success(request):

    return render(
        request,
        'citizen/success.html'
    )


# ==============================
# Citizen List + Search
# ==============================

def citizen_list(request):

    search = request.GET.get('search', '').strip()

    citizens = Citizen.objects.all().order_by('-created_at')

    if search:

        citizens = citizens.filter(
            full_name__icontains=search
        ) | citizens.filter(
            mobile_number__icontains=search
        ) | citizens.filter(
            aadhaar_number__icontains=search
        ) | citizens.filter(
            city__icontains=search
        ) | citizens.filter(
            district__icontains=search
        )

    return render(
        request,
        'citizen/citizen_list.html',
        {
            'citizens': citizens,
            'search': search
        }
    )


# ==============================
# Citizen Details
# ==============================

def citizen_detail(request, citizen_id):

    citizen = get_object_or_404(
        Citizen,
        id=citizen_id
    )

    return render(
        request,
        'citizen/citizen_detail.html',
        {
            'citizen': citizen
        }
    )


# ==============================
# Edit Citizen
# ==============================

def citizen_edit(request, citizen_id):

    citizen = get_object_or_404(
        Citizen,
        id=citizen_id
    )

    if request.method == 'POST':

        form = CitizenForm(
            request.POST,
            instance=citizen
        )

        if form.is_valid():

            form.save()

            return redirect(
                'citizen_detail',
                citizen_id=citizen.id
            )

    else:

        form = CitizenForm(
            instance=citizen
        )

    return render(
        request,
        'citizen/edit.html',
        {
            'form': form,
            'citizen': citizen
        }
    )


# ==============================
# Delete Citizen
# ==============================

def citizen_delete(request, citizen_id):

    citizen = get_object_or_404(
        Citizen,
        id=citizen_id
    )

    if request.method == 'POST':

        citizen.delete()

        return redirect('citizen_list')

    return render(
        request,
        'citizen/delete.html',
        {
            'citizen': citizen
        }
    )