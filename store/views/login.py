from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.views import View

from ..models import Customer


class Login(View):
    def get(self, request):
        return_url = request.GET.get('return_url')
        return render(request, 'login.html', {'return_url': return_url})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        return_url = request.POST.get('return_url')

        customer = Customer.get_customer_by_email(email)
        if customer and check_password(password, customer.password):
            request.session['customer'] = customer.id
            return redirect(return_url or 'homepage')

        return render(request, 'login.html', {'error': 'Invalid email or password!', 'return_url': return_url})


def logout(request):
    request.session.clear()
    return redirect('login')
