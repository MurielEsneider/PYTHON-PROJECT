from django.shortcuts import render
from django import Error
from appPeliculas.models import Genero, Pelicula
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def agregarGenero(request):
    try:
        nombre = request.POST['txtNombre']
        genero = Genero(genNombre=nombre)
        genero.save()
        mensaje = "Genero Agregado Correctamente"
        
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje": mensaje}
    return JsonResponse(retorno)