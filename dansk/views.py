from django.shortcuts import render, redirect
from django.views import View
from .models import Alfabet, Bogstav#, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Æ, Ø, Å, Alfabet, Ekstra
#from .forms import GætForm, EkstraForm
import random

class Base(View):
    def get(self, request, *args, **kwargs):
        a = Alfabet.objects.filter(bogstav__bogstav__contains='A')
        b = Alfabet.objects.filter(bogstav__bogstav__contains='B')
        context = {
            'a': a,
            'b': b,
        }
        return render(request, 'dansk/info.html', context)

class AView(View):
    def get(self, request, *args, **kwargs):
        a = Alfabet.objects.filter(bogstav__bogstav__contains = 'A')
        context = {
            'a': a
        }
        
        return render(request, 'dansk/danska.html',context) 
    
class BView(View):
    def get(self, request, *args, **kwargs):
        b = Alfabet.objects.filter(bogstav__bogstav__contains='B')
        context = {
            'b': b
        }
        return render(request, 'dansk/danskb.html', context)
