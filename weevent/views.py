from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def account(request):
    return render(request, 'account.html')

def events(request):
    return render(request, 'events.html')

def faq(request):
    return render(request, 'favourites.html')

def llama(request):
    return render(request, 'llama.html')

def map(request):
    return render(request, 'map.html')

def preferences(request):
    return render(request, 'preferences.html')

def favourites(request):
    return render(request, 'favourites.html')