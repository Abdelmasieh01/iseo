from django.contrib import admin
from .models import PartnerUniversity, Application, ContactMessage


@admin.register(PartnerUniversity)
class PartnerUniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'available_slots', 'min_gpa', 'application_deadline']
    list_filter = ['country', 'region']
    search_fields = ['name', 'country']


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['reference_number', 'full_name', 'student_id', 'first_choice', 'status', 'submitted_at']
    list_filter = ['status', 'exchange_semester', 'exchange_year', 'program']
    search_fields = ['full_name', 'student_id', 'reference_number']
    readonly_fields = ['reference_number', 'submitted_at', 'last_updated']
    list_editable = ['status']
    ordering = ['-submitted_at']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'submitted_at', 'is_read']
    list_filter = ['is_read']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['is_read']
