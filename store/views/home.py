from django.shortcuts import render, redirect
from django.views import View

from ..models import Category, Products


class Index(View):
    """Homepage: shows the product catalog (optionally filtered by category)
    and also handles add/remove-from-cart POST requests coming from the
    product listing page."""

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart', {})

        if product:
            pid = str(product)
            quantity = cart.get(pid, 0)
            if remove:
                if quantity <= 1:
                    cart.pop(pid, None)
                else:
                    cart[pid] = quantity - 1
            else:
                cart[pid] = quantity + 1

        request.session['cart'] = cart
        return redirect('homepage')

    def get(self, request):
        categories = Category.get_all_categories()
        category_id = request.GET.get('category')

        if category_id:
            products = Products.get_all_products_by_categoryid(category_id)
        else:
            products = Products.get_all_products()

        cart = request.session.get('cart', {})

        return render(request, 'index.html', {
            'products': products,
            'categories': categories,
            'cart': cart,
            'cart_count': sum(cart.values()) if cart else 0,
        })


def store(request):
    """Alias route (/store/) that shows the same catalog as the homepage."""
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')

    if category_id:
        products = Products.get_all_products_by_categoryid(category_id)
    else:
        products = Products.get_all_products()

    cart = request.session.get('cart', {})

    return render(request, 'index.html', {
        'products': products,
        'categories': categories,
        'cart': cart,
        'cart_count': sum(cart.values()) if cart else 0,
    })
