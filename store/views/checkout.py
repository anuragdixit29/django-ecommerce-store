from django.shortcuts import render, redirect
from django.views import View

from ..models import Customer, Order, Products


class CheckOut(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('cart')

        products = Products.get_products_by_id(list(cart.keys()))
        total = sum(p.price * cart.get(str(p.id), 0) for p in products)

        return render(request, 'checkout.html', {'total': total})

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart', {})

        if not customer or not cart:
            return redirect('cart')

        products = Products.get_products_by_id(list(cart.keys()))
        for product in products:
            Order(
                customer=Customer(id=customer),
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                quantity=cart.get(str(product.id)),
            ).save()

        request.session['cart'] = {}
        return redirect('orders')
