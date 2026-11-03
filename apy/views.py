from django.shortcuts import render

def home(request):
    return render(request, 'apy/home.html')

def biography(request):
    return render(request, 'apy/biography.html')

def facts(request):
    return render(request, 'apy/facts.html')

def city_info(request):
    return render(request, 'apy/city_info.html')

def city_places(request):
    return render(request, 'apy/city_places.html')