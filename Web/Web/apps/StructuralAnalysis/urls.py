from django.urls import path
from . import views

app_name = 'StructuralAnalysis'

urlpatterns = [
    path('', views.index, name='index')
]
