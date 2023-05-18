from django.shortcuts import render

def HomePage(request):
    return render(request, 'index.html',{'title': "PAGE D'ACCUEIL"})