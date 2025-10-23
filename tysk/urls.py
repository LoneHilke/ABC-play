from django.urls import path
from . import views
from .views import Base, TyskaView, TyskbView, TyskCView, TyskDView, TyskEView, TyskFView, TyskGView, TyskHView, TyskIView#, TyskJView, TyskKView, TyskLView, TyskMView, TyskNView, TyskOView, TyskPView, TyskQView, TyskRView, TyskSView, TyskTView, TyskUView, TyskVView, TyskWView, TyskXView, TyskYView, TyskZView, ÆView, ØView, ÅView, GætView, Info, Tilføj

urlpatterns = [
    path('', Base.as_view(), name='base'),
    path('tyska/', TyskaView.as_view(), name='tyska'),
    path('tyskb/', TyskbView.as_view(), name='tyskb'),
    path('tyskc/', TyskCView.as_view(), name='tyskc'),
    path('tyskd/', TyskDView.as_view(), name='tyskd'),
    path('tyske/', TyskEView.as_view(), name='tyske'),
    path('tyskf/', TyskFView.as_view(), name='tyskf'),
    path('tyskg/', TyskGView.as_view(), name='tyskg'),
    path('tyskh/', TyskHView.as_view(), name='tyskh'),
    path('tyski/', TyskIView.as_view(), name='tyski'),

]