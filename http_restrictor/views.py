from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .mixins import RestrictMethodsMixin

class MyRestrictedView(RestrictMethodsMixin, View):
    
    allowed_methods = ['GET', 'Post' ,'Put']
    
    def get(self, request, *args, **kwargs):
        return HttpResponse("This is a GET request.")
    
    def post(self, request, *args, **kwargs):
        return HttpResponse("This is a POST request.")

    def put(self, request, *args, **kwargs):
        return HttpResponse("This is a Put request.")