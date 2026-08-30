from django.shortcuts import render, redirect
from django.views import View

from ..models import Products


class Cart(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        products = Products.get_products_by_id(list(cart.keys())) if cart else []

        cart_items = []
        total = 0
        for product in products:
            quantity = cart.get(str(product.id), 0)
            subtotal = product.price * quantity
            total += subtotal
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })

        return render(request, 'cart.html', {
            'cart_items': cart_items,
            'total': total,
        })

    def post(self, request):
        # Allows quantity update / remove directly from the cart page too.
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart', {})

        if product:
            pid = str(product)
            if remove == 'all':
                cart.pop(pid, None)
            else:
                quantity = cart.get(pid, 0)
                if remove:
                    if quantity <= 1:
                        cart.pop(pid, None)
                    else:
                        cart[pid] = quantity - 1
                else:
                    cart[pid] = quantity + 1

        request.session['cart'] = cart
        return redirect('cart')
