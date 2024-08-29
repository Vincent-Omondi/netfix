# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import RequestedService

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    requested_services = RequestedService.objects.filter(user=request.user).order_by('-date_requested')
    
    context = {
        'form': form,
        'requested_services': requested_services
    }
    return render(request, 'users/profile.html', context)

def company_profile(request, pk):
    company = get_object_or_404(get_user_model(), pk=pk, field_of_work__isnull=False)
    services = company.services.all()
    return render(request, 'users/company_profile.html', {'company': company, 'services': services})