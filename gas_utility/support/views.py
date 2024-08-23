from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_status')
    else:
        form = ServiceRequestForm()
    return render(request, 'support/submit_request.html', {'form': form})

@login_required
def request_status(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'support/request_status.html', {'requests': requests})

@login_required
def request_detail(request, request_id):
    service_request = ServiceRequest.objects.get(pk=request_id)
    return render(request, 'support/request_detail.html', {'request': service_request})

@login_required
def update_request(request, request_id):
    service_request = ServiceRequest.objects.get(pk=request_id)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('request_status')
    else:
        form = ServiceRequestForm(instance=service_request)
    return render(request, 'support/update_request.html', {'form': form})
