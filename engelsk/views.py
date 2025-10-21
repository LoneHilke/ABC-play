from django.shortcuts import render
from django.views import View
from .models import Words, Letter

# Create your views here.
class Base(View):
    def get(self, request, *args, **kwargs):
        enga = Words.objects.filter(letter__letter__contains='enga')
        engb = Words.objects.filter(letter__letter__contains='engb')
        engc = Words.objects.filter(letter__letter__contains='engc')
        engd = Words.objects.filter(letter__letter__contains='engd')
        enge = Words.objects.filter(letter__letter__contains='enge')
        engf = Words.objects.filter(letter__letter__contains='engf')
        engg = Words.objects.filter(letter__letter__contains='engg')
        engh = Words.objects.filter(letter__letter__contains='engh')
        engi = Words.objects.filter(letter__letter__contains='engi')
        engj = Words.objects.filter(letter__letter__contains='engj')
        engk = Words.objects.filter(letter__letter__contains='engk')
        engl = Words.objects.filter(letter__letter__contains='engl')
        engm = Words.objects.filter(letter__letter__contains='engm')
        engn = Words.objects.filter(letter__letter__contains='N')
        engo = Words.objects.filter(letter__letter__contains='O')
        engp = Words.objects.filter(letter__letter__contains='P')
        engq = Words.objects.filter(letter__letter__contains='Q')
        engr = Words.objects.filter(letter__letter__contains='R')
        engs = Words.objects.filter(letter__letter__contains='S')
        engt = Words.objects.filter(letter__letter__contains='T')
        engu = Words.objects.filter(letter__letter__contains='U')
        engv = Words.objects.filter(letter__letter__contains='V')
        engw = Words.objects.filter(letter__letter__contains='W')
        engx = Words.objects.filter(letter__letter__contains='X')
        engy = Words.objects.filter(letter__letter__contains='Y')
        engz = Words.objects.filter(letter__letter__contains='Z')
       
        
        context = {
            'enga': enga,
            'engb': engb,
            'engc': engc,
            'engd': engd,
            'enge': enge,
            'engf': engf,
            'engg': engg,
            'engh': engh,
            'engi': engi,
            'engj': engj,
            'engk': engk,
            'engl': engl,
            'engm': engm,
            'n': engn,
            'o': engo,
            'p': engp,
            'q': engq,
            'r': engr,
            's': engs,
            't': engt,
            'u': engu,
            'v': engv,
            'w': engw,
            'x': engx,
            'y': engy,
            'z': engz,
                        
        }
        return render(request, 'engelsk/info.html')
    
class EngelskAView(View):
    def get(self, request, *args, **kwargs):
        enga = Words.objects.filter(letter__letter__contains = 'enga')
        context = {
            'enga': enga
        }
        return render(request, 'engelsk/engelska.html', context)
    
class EngelskBView(View):
    def get(self, request, *args, **kwargs):
        engb = Words.objects.filter(letter__letter__contains = 'engb')
        context = {
            'engb': engb
        }
        return render(request, 'engelsk/engelskb.html', context)
    
class EngelskCView(View):
    def get(self, request, *args, **kwargs):
        engc = Words.objects.filter(letter__letter__contains = 'engc')
        context = {
            'engc': engc
        }
        return render(request, 'engelsk/engelskc.html', context)   

class EngelskDView(View):
    def get(self, request, *args, **kwargs):
        engd = Words.objects.filter(letter__letter__contains = 'engd')
        context = {
            'engd': engd
        }
        return render(request, 'engelsk/engelskd.html', context) 
    
class EngelskEView(View):
    def get(self, request, *args, **kwargs):
        enge = Words.objects.filter(letter__letter__contains = 'enge')
        context = {
            'enge': enge
        }
        return render(request, 'engelsk/engelske.html', context)
    
class EngelskFView(View):
    def get(self, request, *args, **kwargs):
        engf = Words.objects.filter(letter__letter__contains = 'engf')
        context = {
            'engf': engf
        }
        return render(request, 'engelsk/engelskf.html', context)
    
class EngelskGView(View):
    def get(self, request, *args, **kwargs):
        engg = Words.objects.filter(letter__letter__contains = 'engg')
        context = {
            'engg': engg
        }
        return render(request, 'engelsk/engelskg.html', context)
    
class EngelskHView(View):
    def get(self, request, *args, **kwargs):
        engh = Words.objects.filter(letter__letter__contains = 'engh')
        context = {
            'engb': engh
        }
        return render(request, 'engelsk/engelskh.html', context)
    
class EngelskIView(View):
    def get(self, request, *args, **kwargs):
        engi = Words.objects.filter(letter__letter__contains = 'engi')
        context = {
            'engi': engi
        }
        return render(request, 'engelsk/engelski.html', context)   

class EngelskJView(View):
    def get(self, request, *args, **kwargs):
        engj = Words.objects.filter(letter__letter__contains = 'engj')
        context = {
            'engj': engj
        }
        return render(request, 'engelsk/engelskd.html', context) 
    
class EngelskKView(View):
    def get(self, request, *args, **kwargs):
        engk = Words.objects.filter(letter__letter__contains = 'engk')
        context = {
            'engk': engk
        }
        return render(request, 'engelsk/engelskk.html', context)
    
class EngelskLView(View):
    def get(self, request, *args, **kwargs):
        engl = Words.objects.filter(letter__letter__contains = 'engl')
        context = {
            'engl': engl
        }
        return render(request, 'engelsk/engelskl.html', context)
    
class EngelskMView(View):
    def get(self, request, *args, **kwargs):
        engm = Words.objects.filter(letter__letter__contains = 'engm')
        context = {
            'engm': engm
        }
        return render(request, 'engelsk/engelskm.html', context)


