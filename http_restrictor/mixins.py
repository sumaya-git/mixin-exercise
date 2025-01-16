from django.http import HttpResponseForbidden

class RestrictMethodsMixin:
    allowed_methods = ['GET']  # Default to only allow GET requests

    def dispatch(self, request, *args, **kwargs):
        if request.method not in self.allowed_methods:
            return HttpResponseForbidden(self.allowed_methods)
        return super().dispatch(request, *args, **kwargs)
