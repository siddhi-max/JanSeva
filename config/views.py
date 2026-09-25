from django.shortcuts import render
from citizen.models import Citizen


# ==============================
# Dashboard
# ==============================

def dashboard(request):

    total_citizens = Citizen.objects.count()

    pending_citizens = Citizen.objects.filter(
        status='Pending'
    ).count()

    processing_citizens = Citizen.objects.filter(
        status='Processing'
    ).count()

    approved_citizens = Citizen.objects.filter(
        status='Approved'
    ).count()

    rejected_citizens = Citizen.objects.filter(
        status='Rejected'
    ).count()

    completed_citizens = Citizen.objects.filter(
        status='Completed'
    ).count()

    return render(
        request,
        'dashboard.html',
        {
            'total_citizens': total_citizens,
            'pending_citizens': pending_citizens,
            'processing_citizens': processing_citizens,
            'approved_citizens': approved_citizens,
            'rejected_citizens': rejected_citizens,
            'completed_citizens': completed_citizens,
        }
    )


# ==============================
# Reports
# ==============================

def reports(request):

    search = request.GET.get(
        'search',
        ''
    ).strip()

    status = request.GET.get(
        'status',
        ''
    ).strip()


    # All citizens

    citizens = Citizen.objects.all().order_by(
        '-created_at'
    )


    # Search

    if search:

        citizens = citizens.filter(
            full_name__icontains=search
        ) | citizens.filter(
            mobile_number__icontains=search
        ) | citizens.filter(
            city__icontains=search
        ) | citizens.filter(
            district__icontains=search
        )


    # Status Filter

    if status:

        citizens = citizens.filter(
            status=status
        )


    # Summary counts

    total_citizens = Citizen.objects.count()

    pending_citizens = Citizen.objects.filter(
        status='Pending'
    ).count()

    processing_citizens = Citizen.objects.filter(
        status='Processing'
    ).count()

    approved_citizens = Citizen.objects.filter(
        status='Approved'
    ).count()

    rejected_citizens = Citizen.objects.filter(
        status='Rejected'
    ).count()

    completed_citizens = Citizen.objects.filter(
        status='Completed'
    ).count()


    return render(
        request,
        'reports.html',
        {
            'total_citizens': total_citizens,

            'pending_citizens':
                pending_citizens,

            'processing_citizens':
                processing_citizens,

            'approved_citizens':
                approved_citizens,

            'rejected_citizens':
                rejected_citizens,

            'completed_citizens':
                completed_citizens,

            'citizens': citizens,

            'search': search,

            'selected_status': status,
        }
    )