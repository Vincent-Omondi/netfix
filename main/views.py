# main/views.py

from django.shortcuts import render
from services.models import Service

def home(request):
    latest_services = Service.objects.order_by('-date_created')[:5]
    return render(request, 'main/home.html', {'latest_services': latest_services})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')