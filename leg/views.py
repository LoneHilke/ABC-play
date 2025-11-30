from django.shortcuts import render, redirect
from django.views import View
from dansk.models import  Alfabet, Bogstav
from .forms import GætForm
import random

class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'leg/base.html')
    
class Stavda(View):
    def get(self, request, *args, **kwargs):
        
        alfabet = random.choice(Alfabet.objects.all())
        a = random.choice(Alfabet.objects.all())
        b = random.choice(Alfabet.objects.all())
        c = random.choice(Alfabet.objects.all())
        d = random.choice(Alfabet.objects.all())
        e = random.choice(Alfabet.objects.all())
        f = random.choice(Alfabet.objects.all())
        g = random.choice(Alfabet.objects.all())
        h = random.choice(Alfabet.objects.all())
        i = random.choice(Alfabet.objects.all())
        j = random.choice(Alfabet.objects.all())
        k = random.choice(Alfabet.objects.all())
        l = random.choice(Alfabet.objects.all())
        m = random.choice(Alfabet.objects.all())
        n = random.choice(Alfabet.objects.all())
        o = random.choice(Alfabet.objects.all())
        p = random.choice(Alfabet.objects.all())
        q = random.choice(Alfabet.objects.all())
        form = GætForm()
        return render(request, 'leg/stavda.html', {
            'alfabet': alfabet, "a":a, "b":b, "c":c, "d":d,"e":e,"f":f,"g":g,"h":h,"i":i, "j":j,
            "k":k, "l":l, "m":m, "n":n, "o":o, "p":p, "q":q,
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = GætForm(request.POST)
        Bogstav = None
        resultat = None
        aktiv_model = None
        aktiv_id = None

    # Find ud af hvilken form der blev sendt
        if 'alfabet_id' in request.POST:
            aktiv_model = 'alfabet'
            aktiv_id = request.POST.get('alfabet_id')
            obj = Alfabet.objects.get(id=aktiv_id)

        elif 'a_id' in request.POST:
            aktiv_model = 'a/alfabet'
            aktiv_id = request.POST.get('a_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'b_id' in request.POST:
            aktiv_model = 'b/alfabet'
            aktiv_id = request.POST.get('b_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'c_id' in request.POST:
            aktiv_model = 'c/alfabet'
            aktiv_id = request.POST.get('c_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'd_id' in request.POST:
            aktiv_model = 'd/alfabet'
            aktiv_id = request.POST.get('d_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'e_id' in request.POST:
            aktiv_model = 'e/alfabet'
            aktiv_id = request.POST.get('e_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'f_id' in request.POST:
            aktiv_model = 'f/alfabet'
            aktiv_id = request.POST.get('f_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'g_id' in request.POST:
            aktiv_model = 'g/alfabet'
            aktiv_id = request.POST.get('g_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'h_id' in request.POST:
            aktiv_model = 'h/alfabet'
            aktiv_id = request.POST.get('h_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        if 'i_id' in request.POST:
            aktiv_model = 'i/alfabet'
            aktiv_id = request.POST.get('i_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'j_id' in request.POST:
            aktiv_model = 'j/alfabet'
            aktiv_id = request.POST.get('j_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'k_id' in request.POST:
            aktiv_model = 'k/alfabet'
            aktiv_id = request.POST.get('k_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'l_id' in request.POST:
            aktiv_model = 'l/alfabet'
            aktiv_id = request.POST.get('l_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'm_id' in request.POST:
            aktiv_model = 'm/alfabet'
            aktiv_id = request.POST.get('m_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'n_id' in request.POST:
            aktiv_model = 'n/alfabet'
            aktiv_id = request.POST.get('n_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'o_id' in request.POST:
            aktiv_model = 'o/alfabet'
            aktiv_id = request.POST.get('o_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'p_id' in request.POST:
            aktiv_model = 'p/alfabet'
            aktiv_id = request.POST.get('p_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'q_id' in request.POST:
            aktiv_model = 'q/alfabet'
            aktiv_id = request.POST.get('q_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        else:
            obj = None

    # Vurder gæt
        if obj and form.is_valid():
            gæt = form.cleaned_data['gæt'].strip().lower()
            korrekt = obj.ord.strip().lower()

            if gæt == korrekt:
                resultat = "✅ Korrekt!"
                # Vælg et nyt billede efter korrekt 
                if aktiv_model == 'alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'a/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'b/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'c/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'd/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'e/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'f/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'g/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'h/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'i/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'j/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'k/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'l/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'm/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'n/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'o/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'p/alfabet':
                    obj = random.choice(Alfabet.objects.all())
                elif aktiv_model == 'q/alfabet':
                    obj = random.choice(Alfabet.objects.all())
            else:
                resultat = f"❌ Forkert. Det rigtige svar er: {obj.ord}"

        # Alt indhold
            context = {
                'Alfabet':random.choice(Alfabet.objects.all()),
                'a': random.choice(Alfabet.objects.all()),
                'b': random.choice(Alfabet.objects.all()),
                'c': random.choice(Alfabet.objects.all()),
                'd': random.choice(Alfabet.objects.all()),
                'e': random.choice(Alfabet.objects.all()),
                'f': random.choice(Alfabet.objects.all()),
                'g': random.choice(Alfabet.objects.all()),
                'h': random.choice(Alfabet.objects.all()),
                'i': random.choice(Alfabet.objects.all()),
                'j': random.choice(Alfabet.objects.all()),
                'k': random.choice(Alfabet.objects.all()),
                'l': random.choice(Alfabet.objects.all()),
                'm': random.choice(Alfabet.objects.all()),
                'n': random.choice(Alfabet.objects.all()),
                'o': random.choice(Alfabet.objects.all()),
                'p': random.choice(Alfabet.objects.all()),
                'q': random.choice(Alfabet.objects.all()),
                
                'Bogstav':Bogstav,
                'form': form,
                'resultat': resultat,
                'aktiv_model': aktiv_model,
                'aktiv_id': int(aktiv_id) if aktiv_id else None,
            }

            return render(request, 'leg/stavda.html', context)
        

    
