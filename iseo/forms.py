from django import forms
from .models import Application, ContactMessage
from datetime import date


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'full_name', 'student_id', 'email', 'nationality',
            'passport_number', 'passport_expiry',
            'current_gpa', 'program', 'academic_level',
            'first_choice', 'second_choice',
            'exchange_semester', 'exchange_year',
            'language_proficiency', 'personal_statement',
        ]
        widgets = {
            'passport_expiry': forms.DateInput(attrs={'type': 'date'}),
            'personal_statement': forms.Textarea(attrs={'rows': 5}),
            'full_name': forms.TextInput(attrs={'placeholder': 'e.g. Sarah Almutairi'}),
            'student_id': forms.TextInput(attrs={'placeholder': 'e.g. 2221175012'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@university.edu.kw'}),
            'nationality': forms.TextInput(attrs={'placeholder': 'e.g. Kuwaiti'}),
            'passport_number': forms.TextInput(attrs={'placeholder': 'Passport number'}),
            'current_gpa': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01', 'min': '0', 'max': '4'}),
            'academic_level': forms.TextInput(attrs={'placeholder': 'e.g. 3rd Year'}),
            'language_proficiency': forms.TextInput(attrs={'placeholder': 'e.g. TOEFL iBT 100 / IELTS 7.5'}),
            'exchange_year': forms.NumberInput(attrs={'placeholder': '2026', 'min': '2025', 'max': '2030'}),
        }
        labels = {
            'full_name': 'Full Name',
            'student_id': 'Student ID',
            'current_gpa': 'Current GPA (out of 4.0)',
            'first_choice': 'First Choice University',
            'second_choice': 'Second Choice University (optional)',
            'exchange_semester': 'Exchange Semester',
            'exchange_year': 'Exchange Year',
            'language_proficiency': 'Language Proficiency',
            'personal_statement': 'Personal Statement',
        }

    def clean_current_gpa(self):
        gpa = self.cleaned_data.get('current_gpa')
        if gpa and (gpa < 0 or gpa > 4):
            raise forms.ValidationError("GPA must be between 0.00 and 4.00")
        return gpa

    def clean_passport_expiry(self):
        expiry = self.cleaned_data.get('passport_expiry')
        if expiry and expiry <= date.today():
            raise forms.ValidationError("Passport must not be expired.")
        return expiry


class StatusCheckForm(forms.Form):
    reference_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. ISEO-123456',
            'class': 'form-control'
        }),
        label='Application Reference Number'
    )
    student_id = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. 2221175012',
            'class': 'form-control'
        }),
        label='Student ID'
    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'subject': forms.TextInput(attrs={'placeholder': 'How can we help?'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your message here...'}),
        }
