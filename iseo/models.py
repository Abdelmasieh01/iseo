from django.db import models
from django.utils import timezone


class PartnerUniversity(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True)
    language_requirement = models.CharField(max_length=200, blank=True)
    available_slots = models.PositiveIntegerField(default=5)
    application_deadline = models.DateField(null=True, blank=True)
    min_gpa = models.DecimalField(max_digits=3, decimal_places=2, default=3.00)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ['country', 'name']
        verbose_name_plural = 'Partner Universities'

    def __str__(self):
        return f"{self.name} ({self.country})"


class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('waitlisted', 'Waitlisted'),
    ]

    PROGRAM_CHOICES = [
        ('undergraduate', 'Undergraduate'),
        ('graduate', 'Graduate'),
    ]

    SEMESTER_CHOICES = [
        ('fall', 'Fall'),
        ('spring', 'Spring'),
        ('summer', 'Summer'),
    ]

    # Personal Info
    full_name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=20)
    email = models.EmailField()
    nationality = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=50)
    passport_expiry = models.DateField()

    # Academic Info
    current_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    program = models.CharField(max_length=20, choices=PROGRAM_CHOICES)
    academic_level = models.CharField(max_length=100)  # e.g. "3rd Year"

    # Exchange Preferences
    first_choice = models.ForeignKey(
        PartnerUniversity, on_delete=models.SET_NULL,
        null=True, related_name='first_choice_applications'
    )
    second_choice = models.ForeignKey(
        PartnerUniversity, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='second_choice_applications'
    )
    exchange_semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    exchange_year = models.PositiveIntegerField()

    # Documents (just filenames for demo)
    transcript = models.FileField(upload_to='documents/', null=True, blank=True)
    passport_copy = models.FileField(upload_to='documents/', null=True, blank=True)
    personal_statement = models.TextField()
    language_proficiency = models.CharField(max_length=200)  # e.g. "TOEFL 105"

    # System fields
    reference_number = models.CharField(max_length=20, unique=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    admin_notes = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.reference_number:
            import random
            import string
            self.reference_number = 'ISEO-' + ''.join(
                random.choices(string.digits, k=6)
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_number} - {self.full_name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"
