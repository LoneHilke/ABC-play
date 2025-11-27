from django.shortcuts import render, redirect
from django.views import View
from .models import Alfabeth, Bugstab#, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Æ, Ø, Å, Alfabet, Ekstra
from .forms import GætForm, EkstraForm
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
        e = Alfabeth.objects.filter(bugstab__bugstab__contains='E')
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
    
class TyskJView(View):
    def get(self, request, *args, **kwargs):
        j = Alfabeth.objects.filter(bugstab__bugstab__contains='J')
        context = {
            'j': j
        }
        return render(request, 'tysk/tyskj.html', context)
    
class TyskKView(View):
    def get(self, request, *args, **kwargs):
        k = Alfabeth.objects.filter(bugstab__bugstab__contains='K')
        context = {
            'k': k
        }
        return render(request, 'tysk/tyskk.html', context)
    
class TyskLView(View):
    def get(self, request, *args, **kwargs):
        l = Alfabeth.objects.filter(bugstab__bugstab__contains='L')
        context = {
            'l': l
        }
        return render(request, 'tysk/tyskl.html', context)
    
class TyskMView(View):
    def get(self, request, *args, **kwargs):
        m = Alfabeth.objects.filter(bugstab__bugstab__contains='M')
        context = {
            'm': m
        }
        return render(request, 'tysk/tyskm.html', context)
    
class TyskNView(View):
    def get(self, request, *args, **kwargs):
        n = Alfabeth.objects.filter(bugstab__bugstab__contains='N')
        context = {
            'n': n
        }
        return render(request, 'tysk/tyskn.html', context)
    
class TyskOView(View):
    def get(self, request, *args, **kwargs):
        o = Alfabeth.objects.filter(bugstab__bugstab__contains='O')
        context = {
            'o': o
        }
        return render(request, 'tysk/tysko.html', context)
    
class TyskPView(View):
    def get(self, request, *args, **kwargs):
        p = Alfabeth.objects.filter(bugstab__bugstab__contains='P')
        context = {
            'p': p
        }
        return render(request, 'tysk/tyskp.html', context)
    
class TyskQView(View):
    def get(self, request, *args, **kwargs):
        q = Alfabeth.objects.filter(bugstab__bugstab__contains='Q')
        context = {
            'q': q
        }
        return render(request, 'tysk/tyskq.html', context)
    
class TyskRView(View):
    def get(self, request, *args, **kwargs):
        r = Alfabeth.objects.filter(bugstab__bugstab__contains='R')
        context = {
            'r': r
        }
        return render(request, 'tysk/tyskr.html', context)
    
class TyskSView(View):
    def get(self, request, *args, **kwargs):
        s = Alfabeth.objects.filter(bugstab__bugstab__contains='S')
        context = {
            's': s
        }
        return render(request, 'tysk/tysks.html', context)
    
class TyskTView(View):
    def get(self, request, *args, **kwargs):
        t = Alfabeth.objects.filter(bugstab__bugstab__contains='T')
        context = {
            't': t
        }
        return render(request, 'tysk/tyskt.html', context)
    
class TyskUView(View):
    def get(self, request, *args, **kwargs):
        u = Alfabeth.objects.filter(bugstab__bugstab__contains='U')
        context = {
            'u': u
        }
        return render(request, 'tysk/tysku.html', context)
    
class TyskVView(View):
    def get(self, request, *args, **kwargs):
        v = Alfabeth.objects.filter(bugstab__bugstab__contains='V')
        context = {
            'v': v
        }
        return render(request, 'tysk/tyskv.html', context)
    
class TyskWView(View):
    def get(self, request, *args, **kwargs):
        w = Alfabeth.objects.filter(bugstab__bugstab__contains='W')
        context = {
            'w': w
        }
        return render(request, 'tysk/tyskw.html', context)
    
class TyskXView(View):
    def get(self, request, *args, **kwargs):
        x = Alfabeth.objects.filter(bugstab__bugstab__contains='X')
        context = {
            'x': x
        }
        return render(request, 'tyskx.html', context)
    
class TyskYView(View):
    def get(self, request, *args, **kwargs):
        yr = Alfabeth.objects.filter(bugstab__bugstab__contains='Y')
        context = {
            'y': y
        }
        return render(request, 'tysk/tysky.html', context)

class TyskZView(View):
    def get(self, request, *args, **kwargs):
        z = Alfabeth.objects.filter(bugstab__bugstab__contains='Z')
        context = {
            'z': z
        }
        return render(request, 'tysk/tyskz.html', context)
    
class Tilføj(View):
    def get(self, request, *args, **kwargs):
        form = EkstraForm()
        alfabeth = Alfabeth.objects.all()
        return render(request, 'tysk/tyskplus.html', {
            'form': form,
            'alfabeth': alfabeth,
        })

    def post(self, request, *args, **kwargs):
        form = EkstraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/tysk/tyskplus')

        alfabeth = Alfabeth.objects.all()
        return render(request, 'tysk/tyskplus.html', {
            'form': form,
            'alfabeth': alfabeth,
        })







