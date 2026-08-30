# ShopEasy — Django E-commerce Website

A simple e-commerce web app built with Django where users can browse a product
catalog, manage a session-based cart, sign up/login, checkout, and view their
order history. Admins manage products/categories/orders via the Django admin.

## Features
- Browse products, filter by category
- Add / remove / update cart item quantities (session-based cart)
- Signup & login with hashed passwords (`django.contrib.auth.hashers`)
- Auth-protected cart, checkout & orders pages (custom `auth_middleware`)
- Checkout converts cart into `Order` records tied to the logged-in customer
- Order history per customer
- Django admin for managing Categories, Products, Customers, Orders

## Tech Stack
- Python 3, Django, SQLite (default dev DB), Pillow (for product images)

## Project Structure
```
ecommerce_project/     # Django project (settings, root urls)
store/
  models/              # Category, Customer, Products, Order
  views/                # home, signup, login, cart, checkout, orders
  middlewares/auth.py   # auth_middleware — protects cart/checkout/orders
  templates/            # base.html, index.html, login.html, signup.html, cart.html, checkout.html, orders.html
  static/store/css/     # style.css
  templatetags/         # store_extras.py (get_item filter for cart lookups)
  admin.py              # admin registrations
  urls.py               # app routes
```

## Setup

```bash
# 1. Create & activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py makemigrations
python manage.py migrate

# 4. Create an admin user
python manage.py createsuperuser

# 5. Run the dev server
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** for the store, and
**http://127.0.0.1:8000/admin/** to add Categories and Products (with images)
before browsing the catalog.

## Customer Workflow
Browse products → change quantity in cart → checkout (login required) → view order history.

## Admin Workflow
Login to `/admin/` → add categories → add products (name, price, category, image) → manage orders.
