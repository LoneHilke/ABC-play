from django.urls import path
from . import views
from .views import Base, Stavda

urlpatterns = [
    path('', Base.as_view(), name='base'),
    path("stavda/", Stavda.as_view(), name='stavda'),
    
]