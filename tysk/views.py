from django.shortcuts import render, redirect
from django.views import View
from .models import Alfabeth, Bugstab#, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Æ, Ø, Å, Alfabet, Ekstra
#from .forms import GætForm, EkstraForm
import random

class Base(View):
    def get(self, request, *args, **kwargs):
        a = Alfabeth.objects.filter(bugstab__bugstab__contains='A')
        b = Alfabeth.objects.filter(bugstab__bugstab__contains='B')
        c = Alfabeth.objects.filter(bugstab__bugstab__contains='C')
        d = Alfabeth.objects.filter(bugstab__bugstab__contains='D')
        e = Alfabeth.objects.filter(bugstab__bugstab__contains='E')
        f = Alfabeth.objects.filter(bugstab__bugstab__contains='F')
        g = Alfabeth.objects.filter(bugstab__bugstab__contains='G')
        h = Alfabeth.objects.filter(bugstab__bugstab__contains='H')
        i = Alfabeth.objects.filter(bugstab__bugstab__contains='I')
        j = Alfabeth.objects.filter(bugstab__bugstab__contains='J')
        k = Alfabeth.objects.filter(bugstab__bugstab__contains='K')
        l = Alfabeth.objects.filter(bugstab__bugstab__contains='L')
        m = Alfabeth.objects.filter(bugstab__bugstab__contains='M')
        n = Alfabeth.objects.filter(bugstab__bugstab__contains='N')
        o = Alfabeth.objects.filter(bugstab__bugstab__contains='O')
        p = Alfabeth.objects.filter(bugstab__bugstab__contains='P')
        q = Alfabeth.objects.filter(bugstab__bugstab__contains='Q')
        r = Alfabeth.objects.filter(bugstab__bugstab__contains='R')
        s = Alfabeth.objects.filter(bugstab__bugstab__contains='S')
        t = Alfabeth.objects.filter(bugstab__bugstab__contains='T')
        u = Alfabeth.objects.filter(bugstab__bugstab__contains='U')
        v = Alfabeth.objects.filter(bugstab__bugstab__contains='V')
        w = Alfabeth.objects.filter(bugstab__bugstab__contains='W')
        x = Alfabeth.objects.filter(bugstab__bugstab__contains='X')
        y = Alfabeth.objects.filter(bugstab__bugstab__contains='Y')
        z = Alfabeth.objects.filter(bugstab__bugstab__contains='Z')
        
        
        context = {
            'a': a,
            'b': b,
            'c': c,
            'd': d,
            'e': e,
            'f': f,
            'g': g,
            'h': h,
            'i': i,
            'j': j,
            'k': k,
            'l': l,
            'm': m,
            'n': n,
            'o': o,
            'p': p,
            'q': q,
            'r': r,
            's': s,
            't': t,
            'u': u,
            'v': v,
            'w': w,
            'x': x,
            'y': y,
            'z': z,
            
            
        }
        return render(request, 'tysk/info.html', context)

class TyskaView(View):
    def get(self, request, *args, **kwargs):
        a = Alfabeth.objects.filter(bugstab__bugstab__contains = 'A')
        context = {
            'a': a
        }
        
        return render(request, 'tysk/tyska.html',context) 
    
class TyskbView(View):
    def get(self, request, *args, **kwargs):
        b = Alfabeth.objects.filter(bugstab__bugstab__contains='B')
        context = {
            'b': b
        }
        return render(request, 'tysk/tyskb.html', context)
    
class TyskCView(View):
    def get(self, request, *args, **kwargs):
        c = Alfabeth.objects.filter(bugstab__bugstab__contains='C')
        context = {
            'c': c
        }
        return render(request, 'tysk/tyskc.html', context)
    
class TyskDView(View):
    def get(self, request, *args, **kwargs):
        d = Alfabeth.objects.filter(bugstab__bugstab__contains='D')
        context = {
            'd': d
        }
        return render(request, 'tysk/tyskd.html', context)
    
class TyskEView(View):
    def get(self, request, *args, **kwargs):
        e = Alfabeth.objects.filter(bugstab__bugstab__contains='e')
        context = {
            'e': e
        }
        return render(request, 'tysk/tyske.html', context)
    
class TyskFView(View):
    def get(self, request, *args, **kwargs):
        f = Alfabeth.objects.filter(bugstab__bugstab__contains='F')
        context = {
            'f': f
        }
        return render(request, 'tysk/tyskf.html', context)
    
class TyskGView(View):
    def get(self, request, *args, **kwargs):
        g = Alfabeth.objects.filter(bugstab__bugstab__contains='G')
        context = {
            'g': g
        }
        return render(request, 'tysk/tyskg.html', context)
    
class TyskHView(View):
    def get(self, request, *args, **kwargs):
        h = Alfabeth.objects.filter(bugstab__bugstab__contains='H')
        context = {
            'h': h
        }
        return render(request, 'tysk/tyskh.html', context)
    
class TyskIView(View):
    def get(self, request, *args, **kwargs):
        i = Alfabeth.objects.filter(bugstab__bugstab__contains='I')
        context = {
            'i': i
        }
        return render(request, 'tysk/tyski.html', context)

