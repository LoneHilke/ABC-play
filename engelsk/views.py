from django.shortcuts import render
from django.views import View

# Create your views here.
class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'engelsk/info.html')
    
class EngelskAView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'engelsk/engelska.html')
    
class EngelskBView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'engelsk/engelskb.html')


