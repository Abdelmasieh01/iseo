from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('apply/', views.apply, name='apply'),
    path('apply/success/<str:ref>/', views.apply_success, name='apply_success'),
    path('track/', views.track_status, name='track_status'),
    path('contact/', views.contact, name='contact'),
    path('eligibility/', views.eligibility, name='eligibility'),
]
