from django.shortcuts import render
from django.http import HttpResponse
'''from .forms import CompteUtilisateur
from django.contrib import messages'''

def Index(request):
    return render(request, "Utilisateurs/index.html")

def Inscription(request):
    return render(request, 'Utilisateurs/inscription.html')

def Connexion(request):
    return render(request, 'Utilisateurs/connexion.html')

def Profil(request):
    return render(request, 'Utilisateurs/profil.html')
