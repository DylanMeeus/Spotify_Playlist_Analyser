from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . import algorithm

def index(request):
    analysis = algorithm.Analyser('Insanity0107')
    template = loader.get_template('analysis/index.html')
    context = {
        'playlists' : analysis.user_playlists,
    }
    return render(request,'analysis/index.html',context)

