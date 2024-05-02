from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


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

from django.contrib.auth.models import User


@login_required
def edit_profile(request):
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return redirect('create_profile')

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, instance=customer)
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if customer_form.is_valid() and user_form.is_valid():
            customer_form.save()
            user_form.save()
            return redirect('view_profile')
    else:
        customer_form = CustomerForm(instance=customer)
        user_form = CustomUserChangeForm(instance=request.user)

    context = {
        'customer_form': customer_form,
        'user_form': user_form,
    }
    return render(request, 'index/edit_profile.html', context)

