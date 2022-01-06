from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator


class StaffRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request, "")
            return redirect(settings.LOGIN_URL)

        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class SuperUserRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, "")
            return redirect(settings.LOGIN_URL)

        return super(SuperUserRequiredMixin, self).dispatch(request, *args, **kwargs)
