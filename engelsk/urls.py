from django.urls import path
from . import views
from .views import Base, EngelskAView, EngelskBView#, CView, DView, EView, FView, GView, HView, IView, JView, KView, LView, MView, NView, OView, PView, QView, RView, SView, TView, UView, VView, WView, XView, YView, ZView, ÆView, ØView, ÅView, GætView, Info, Tilføj

urlpatterns = [
    path('', Base.as_view(), name='base'),
    path('engelska/', EngelskAView.as_view(), name='engelska'),
    path('engelskb/', EngelskBView.as_view(), name='engelskb'),
]