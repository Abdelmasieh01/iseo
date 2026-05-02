from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import PartnerUniversity, Application, ContactMessage
from .forms import ApplicationForm, StatusCheckForm, ContactForm


def home(request):
    universities = PartnerUniversity.objects.all()[:6]
    total_partners = PartnerUniversity.objects.count()
    return render(request, 'iseo/home.html', {
        'universities': universities,
        'total_partners': total_partners,
    })


def about(request):
    return render(request, 'iseo/about.html')


def programs(request):
    country_filter = request.GET.get('country', '')
    universities = PartnerUniversity.objects.all()
    if country_filter:
        universities = universities.filter(country__icontains=country_filter)
    countries = PartnerUniversity.objects.values_list('country', flat=True).distinct().order_by('country')
    return render(request, 'iseo/programs.html', {
        'universities': universities,
        'countries': countries,
        'selected_country': country_filter,
    })


def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            messages.success(
                request,
                f'Application submitted! Reference: <strong>{application.reference_number}</strong>'
            )
            return redirect('apply_success', ref=application.reference_number)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ApplicationForm()
    return render(request, 'iseo/apply.html', {'form': form})


def apply_success(request, ref):
    application = get_object_or_404(Application, reference_number=ref)
    return render(request, 'iseo/apply_success.html', {'application': application})


def track_status(request):
    application = None
    error = None
    STATUS_FLOW = [
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('accepted', 'Decision Made'),
    ]

    if request.method == 'POST':
        form = StatusCheckForm(request.POST)
        if form.is_valid():
            ref = form.cleaned_data['reference_number'].strip().upper()
            sid = form.cleaned_data['student_id'].strip()
            try:
                application = Application.objects.get(reference_number=ref, student_id=sid)
            except Application.DoesNotExist:
                error = 'No application found. Please check your reference number and student ID.'
    else:
        form = StatusCheckForm()

    statuses = []
    if application:
        order = ['pending', 'under_review', 'accepted']
        current = application.status
        if current in ('rejected', 'waitlisted'):
            current_idx = 2
        else:
            current_idx = order.index(current) if current in order else 0
        for i, (s, label) in enumerate(STATUS_FLOW):
            statuses.append((s, label, i <= current_idx))

    return render(request, 'iseo/track_status.html', {
        'form': form,
        'application': application,
        'error': error,
        'statuses': statuses,
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent! We'll get back to you within 2-3 business days.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'iseo/contact.html', {'form': form})


def eligibility(request):
    return render(request, 'iseo/eligibility.html')
