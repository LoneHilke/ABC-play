from django.urls import path
from . import views
from .views import Base, TyskaView, TyskbView#, CView, DView, EView, FView, GView, HView, IView, JView, KView, LView, MView, NView, OView, PView, QView, RView, SView, TView, UView, VView, WView, XView, YView, ZView, ÆView, ØView, ÅView, GætView, Info, Tilføj

urlpatterns = [
    path('', Base.as_view(), name='base'),
    path('tyska/', TyskaView.as_view(), name='tyska'),
    path('tyskb/', TyskbView.as_view(), name='tyskb'),
]