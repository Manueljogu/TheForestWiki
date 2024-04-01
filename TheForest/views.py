from django.shortcuts import render

# Create your views here.

def menuprincipal_wiki(request):
    return render(request, 'TheForest/menuprincipal_wiki.html')

def Animales(request):
    return render(request, 'TheForest/Animales.html')

def Armas(request):
    return render(request, 'TheForest/Armas.html')

def Construcciones(request):
    return render(request, 'TheForest/Construcciones.html')

def Consumibles(request):
    return render(request, 'TheForest/Consumibles.html')

def Consumibles(request):
    return render(request, 'TheForest/Consumibles.html')

def Enemigos(request):
    return render(request, 'TheForest/Enemigos.html')

def Flora(request):
    return render(request, 'TheForest/Flora.html')

def forowiki(request):
    return render(request, 'TheForest/forowiki.html')

def historia(request):
    return render(request, 'TheForest/historia.html')

def inicio_sesion_wiki(request):
    return render(request, 'TheForest/inicio_sesion_wiki.html')

def Logros(request):
    return render(request, 'TheForest/Logros.html')

def Lugarestf(request):
    return render(request, 'TheForest/Lugarestf.html')

def micuentatf(request):
    return render(request, 'TheForest/micuentatf.html')

def recuperarcontra(request):
    return render(request, 'TheForest/recuperarcontra.html')

def registrase_wiki(request):
    return render(request, 'TheForest/registrase_wiki.html')