from functools import wraps

from django.shortcuts import redirect


def auth_middleware(view):
    """
    Wraps a view (function or class-based .as_view() result) so that it
    only runs if a customer is logged in (present in session).
    Otherwise redirects to the login page with a return_url.
    """

    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('customer'):
            return redirect(f"/login/?return_url={request.path}")
        return view(request, *args, **kwargs)

    return wrapper
