from django.http import HttpResponse
from django.shortcuts import render

app_name = 'StructuralAnalysis'

def index(request):
    return render(request, app_name + '/templates/index.html')
