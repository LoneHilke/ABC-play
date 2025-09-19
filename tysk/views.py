from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tysk/base.html')
    
class TyskaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tysk/tyska.html')
    
class TyskbView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tysk/tyskb.html')
    
