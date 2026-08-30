from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View

from ..models import Customer


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        email = request.POST.get('email')
        customer = Customer(
            first_name=request.POST.get('firstname'),
            last_name=request.POST.get('lastname'),
            phone=request.POST.get('phone'),
            email=email,
            password=request.POST.get('password'),
        )

        if customer.isExists():
            return render(request, 'signup.html', {'error': 'Email already registered!'})

        customer.password = make_password(customer.password)
        customer.register()
        return redirect('login')
