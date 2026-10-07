from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/index.html')

def jdc(request):
    return render(request, 'mainapp/jdc.html')

def mapi(request):
    return render(request, 'mainapp/mapi.html')

def pkmn(request):
    return render(request, 'mainapp/pkmn.html')