from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
from .models import Customer

@login_required
def view_or_edit_profile(request):
    user = request.user
    role = request.user.role
    try:
        customer = Customer.objects.get(user=user)
        edit_url = 'edit_profile'
    except Customer.DoesNotExist:
        customer = None
        edit_url = 'create_profile'

    context = {
        'user': user,
        'user_role': role,
        'customer': customer,
        'edit_url': edit_url,
    }
    return render(request, 'index/customer.html', context)

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('view_profile')
    else:
        form = CustomerForm()

    context = {
        'form': form,
    }
    return render(request, 'index/create_profile.html', context)

@login_required
def edit_profile(request):
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return redirect('create_profile')

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = CustomerForm(instance=customer)

    context = {
        'form': form,
    }
    return render(request, 'index/edit_profile.html', context)
