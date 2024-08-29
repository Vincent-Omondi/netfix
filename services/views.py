# services/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Service
from .forms import ServiceForm, ServiceRequestForm
from users.models import RequestedService

def service_list(request):
    services = Service.objects.all().order_by('-date_created')
    return render(request, 'services/service_list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.service = service
            service_request.save()
            messages.success(request, 'Service request submitted successfully!')
            return redirect('service_detail', pk=pk)
    else:
        form = ServiceRequestForm()
    return render(request, 'services/service_detail.html', {'service': service, 'form': form})

@login_required
def create_service(request):
    if not request.user.is_company():
        messages.error(request, 'Only companies can create services.')
        return redirect('service_list')
    
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.company = request.user
            service.save()
            messages.success(request, 'Service created successfully!')
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceForm()
    return render(request, 'services/create_service.html', {'form': form})

def service_by_category(request, category):
    services = Service.objects.filter(field=category).order_by('-date_created')
    return render(request, 'services/service_list.html', {'services': services, 'category': category})

def most_requested_services(request):
    services = Service.objects.annotate(request_count=models.Count('requestedservice')).order_by('-request_count')[:10]
    return render(request, 'services/most_requested_services.html', {'services': services})