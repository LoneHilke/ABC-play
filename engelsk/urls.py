from django.urls import path
from . import views
from .views import Base, EngelskAView, EngelskBView, EngelskCView, EngelskDView, EngelskEView, EngelskFView, EngelskGView, EngelskHView, EngelskIView, EngelskJView, EngelskKView, EngelskLView, EngelskMView#, EngelskNView, EngelskOView, EngelskPView, EngelskQView, EngelskRView, EngelskSView, EngelskTView, EngelskUView, EngelskVView, EngelskWView, EngelskXView, EngelskYView, EngelskZView, GætView, Info, Tilføj

urlpatterns = [
    path('', Base.as_view(), name='base'),
    path('engelska/', EngelskAView.as_view(), name='engelska'),
    path('engelskb/', EngelskBView.as_view(), name='engelskb'),
    path('engelskc/', EngelskCView.as_view(), name='engelskc'),
    path('engelskd/', EngelskDView.as_view(), name='engelskd'),
    path('engelske/', EngelskEView.as_view(), name='engelske'),
    path('engelskf/', EngelskFView.as_view(), name='engelskf'),
    path('engelskg/', EngelskGView.as_view(), name='engelskg'),
    path('engelskh/', EngelskHView.as_view(), name='engelskh'),
    path('engelski/', EngelskIView.as_view(), name='engelski'),
    path('engelskj/', EngelskJView.as_view(), name='engelskj'),
    path('engelskk/', EngelskKView.as_view(), name='engelskk'),
    path('engelskl/', EngelskLView.as_view(), name='engelskl'),
    path('engelskm/', EngelskMView.as_view(), name='engelskm'),
        
]