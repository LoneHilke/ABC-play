from django.shortcuts import render, redirect
from django.views import View

class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'leg/base.html')