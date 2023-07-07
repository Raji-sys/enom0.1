from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser == False:
            return HttpResponseRedirect(reverse('staff:staffhome'))
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse('ems:auth'))
        return wrapper_func
    return decorator


# def admin_only(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         group=None
#         if request.user.groups.exists():
#             group=request.user.groups.all()[0].name
#         if group=='employee':
#             return redirect('ems:user')
#         if group=='admin':
#             return view_func(request, *args, **kwargs)
#     return wrapper_function
