from django.http import HttpResponseForbidden
from authentication.models import UserProfilePlus


def coaches_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            user_cat = UserProfilePlus.objects.get(user=request.user.id).user_cat
            if user_cat == 'T' or request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("У вас нет прав")
        else:
            return HttpResponseForbidden("У вас нет прав")
    return wrapper