from django.urls import path
from . import views
from .views import Base, AView, BView#, CView, DView, EView, FView, GView, HView, IView, JView, KView, LView, MView, NView, OView, PView, QView, RView, SView, TView, UView, VView, WView, XView, YView, ZView, ÆView, ØView, ÅView, GætView, Info, Tilføj

urlpatterns = [
    path('', Base.as_view(), name='info'),
    path('danska/', AView.as_view(), name='danska'),
    path('danskb/', BView.as_view(), name='danskb'),
]