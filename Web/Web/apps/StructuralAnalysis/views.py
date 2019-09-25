from django.http import HttpResponse
from django.shortcuts import render
from Web.Yargy.Analysis.dateanalysis import ExtractionDate
from Web.Yargy.DataLoader.DataLoader import DataLoader

app_name = 'StructuralAnalysis'

def index(request):
    context = {
        "text": DataLoader().getTextList().pop(0),
        "json": ""
    }
    return render(request, app_name + '/templates/index.html', context)

def get(request):
    text = request.POST['text']
    context = {
        "text": text,
        "json": {
            "data": ExtractionDate().setText(text).getDate()
        }
    }
    return render(request, app_name + '/templates/index.html', context)
