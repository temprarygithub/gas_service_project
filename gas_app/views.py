from django.shortcuts import render, redirect
from .models import User, Service_requests , Support_Representative
from .forms import Service_Request_Form, Track_Status_Form , SupportRepresentativeForm  

def gas(request):
    return render(request, 'gas.html')

def submit_request(request):
    if request.method == 'POST':
        form = Service_Request_Form(request.POST, request.FILES)
        if form.is_valid():
            customer_account = request.POST['account_number']
            customer = User.objects.get(account_number=customer_account)
            form.instance.customer = customer
            form.instance.status = 'Pending'
            form.save()
            return redirect('track_status')
    else:
        form = Service_Request_Form()
    return render(request, 'submit_request.html', {'form': form})

def track_status(request):
    if request.method == 'POST':
        form = Track_Status_Form(request.POST)
        if form.is_valid():
            account_number = form.cleaned_data['account_number']
            customer = User.objects.get(account_number=account_number)
            requests = Service_requests.objects.filter(customer=customer)
            return render(request, 'track_status.html', {'form': form, 'requests': requests})
    else:
        form = Track_Status_Form()
    return render(request, 'track_status.html', {'form': form})


def add_support(request):
    if request.method == 'POST':
        form = SupportRepresentativeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_support_reps')
    else:
        form = SupportRepresentativeForm()
    return render(request, 'add_support.html', {'form': form})

def manage_support_reps(request):
    support_reps = Support_Representative.objects.all()
    return render(request, 'manage_support.html', {'support_reps': support_reps})