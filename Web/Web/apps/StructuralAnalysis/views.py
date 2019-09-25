from django.http import HttpResponse
from django.shortcuts import render

from .Yargy.Analysis.StructuralAnalysis import JSON_RESULT

app_name = 'StructuralAnalysis'

def index(request):
    context = {
        "json" : JSON_RESULT
    }
    return render(request, app_name + '/templates/index.html', context)