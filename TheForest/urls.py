from django.urls import path
from .views import menuprincipal_wiki, Animales, Armas, Construcciones, Consumibles, Enemigos, Flora, forowiki, historia, inicio_sesion_wiki, Logros, Lugarestf, micuentatf, recuperarcontra, registrase_wiki


urlpatterns = [
    path('', menuprincipal_wiki, name="menuprincipal_wiki"),
    path('Animales/', Animales, name="Animales"),
    path('Armas/', Armas, name="Armas"),
    path('Construcciones/', Construcciones, name="Construcciones"),
    path('Consumibles/', Consumibles, name="Consumibles"),
    path('Enemigos/', Enemigos, name="Enemigos"),
    path('Flora/', Flora, name="Flora"),
    path('forowiki/', forowiki, name="forowiki"),
    path('historia/', historia, name="historia"),
    path('inicio_sesion_wiki/', inicio_sesion_wiki, name="inicio_sesion_wiki"),
    path('Logros/', Logros, name="Logros"),
    path('Lugarestf/', Lugarestf, name="Lugarestf"),
    path('micuentatf/', micuentatf, name="micuentatf"),
    path('recueperacontra/', recuperarcontra, name="recuperacontra"),
    path('registrase_wiki/', registrase_wiki, name="registrase_wiki"), 
    
]

