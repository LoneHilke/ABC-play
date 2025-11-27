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
        a = random.choice(Bogstav.objects.all())
        b = random.choice(Bogstav.objects.all())
        c = random.choice(Bogstav.objects.all())
        d = random.choice(Bogstav.objects.all())
        e = random.choice(Bogstav.objects.all())
        f = random.choice(Bogstav.objects.all())
        g = random.choice(Bogstav.objects.all())
        h = random.choice(Bogstav.objects.all())
        form = GætForm()
        return render(request, 'leg/stavda.html', {
            'alfabet': alfabet, "a":a, "b":b,
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = GætForm(request.POST)
        Bogstav = None
        resultat = None
        aktiv_model = None
        aktiv_id = None

    # Find ud af hvilken form der blev sendt
        if 'a_id' in request.POST:
            aktiv_model = 'a'
            aktiv_id = request.POST.get('a_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'b_id' in request.POST:
            aktiv_model = 'b'
            aktiv_id = request.POST.get('b_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'c_id' in request.POST:
            aktiv_model = 'c'
            aktiv_id = request.POST.get('c_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'd_id' in request.POST:
            aktiv_model = 'd'
            aktiv_id = request.POST.get('d_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'e_id' in request.POST:
            aktiv_model = 'e'
            aktiv_id = request.POST.get('e_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'f_id' in request.POST:
            aktiv_model = 'f'
            aktiv_id = request.POST.get('f_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'g_id' in request.POST:
            aktiv_model = 'g'
            aktiv_id = request.POST.get('g_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'h_id' in request.POST:
            aktiv_model = 'h'
            aktiv_id = request.POST.get('h_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        if 'i_id' in request.POST:
            aktiv_model = 'i'
            aktiv_id = request.POST.get('i_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'j_id' in request.POST:
            aktiv_model = 'j'
            aktiv_id = request.POST.get('j_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'k_id' in request.POST:
            aktiv_model = 'k'
            aktiv_id = request.POST.get('k_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'l_id' in request.POST:
            aktiv_model = 'l'
            aktiv_id = request.POST.get('l_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'm_id' in request.POST:
            aktiv_model = 'm'
            aktiv_id = request.POST.get('m_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'n_id' in request.POST:
            aktiv_model = 'n'
            aktiv_id = request.POST.get('n_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'o_id' in request.POST:
            aktiv_model = 'o'
            aktiv_id = request.POST.get('o_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        elif 'p_id' in request.POST:
            aktiv_model = 'p'
            aktiv_id = request.POST.get('p_id')
            obj = Alfabet.objects.get(id=aktiv_id)
        else:
            obj = None

    # Vurder gæt
        if obj and form.is_valid():
            gæt = form.cleaned_data['gæt'].strip().lower()
            korrekt = obj.ord.strip().lower()

            if gæt == korrekt:
                resultat = "✅ Korrekt!"
                # Vælg et nyt billede efter korrekt svar
                if aktiv_model == 'a':
                    obj = random.choice(A.objects.all())
                elif aktiv_model == 'b':
                    obj = random.choice(B.objects.all())
                elif aktiv_model == 'c':
                    obj = random.choice(C.objects.all())
                elif aktiv_model == 'd':
                    obj = random.choice(D.objects.all())
                elif aktiv_model == 'e':
                    obj = random.choice(E.objects.all())
                elif aktiv_model == 'f':
                    obj = random.choice(F.objects.all())
                elif aktiv_model == 'g':
                    obj = random.choice(G.objects.all())
                elif aktiv_model == 'h':
                    obj = random.choice(H.objects.all())
            else:
                resultat = f"❌ Forkert. Det rigtige svar er: {obj.ord}"

        # Alt indhold
            context = {
                'Alfabet':random.choice(Bogstav.objects.all()),
                'a': random.choice(A.objects.all()),
                'b': random.choice(B.objects.all()),
                'c': random.choice(C.objects.all()),
                'd': random.choice(D.objects.all()),
                'e': random.choice(E.objects.all()),
                'f': random.choice(F.objects.all()),
                'g': random.choice(G.objects.all()),
                'h': random.choice(H.objects.all()),
                'Alfabet':Alfabet,
                'Bogstav':Bogstav,
                'form': form,
                'resultat': resultat,
                'aktiv_model': aktiv_model,
                'aktiv_id': int(aktiv_id) if aktiv_id else None,
            }

            return render(request, 'leg/stavda.html', context)
        

    
