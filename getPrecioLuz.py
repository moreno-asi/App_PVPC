"""
En este script obtenemos el precio de la luz de la web indicada en urlBase
"""

import requests
from bs4 import BeautifulSoup

from statistics import mean
import re


urlBase = "https://tarifaluzhora.es/"
#Creamos un objeto request con la url que queremos analizar
miDoc = requests.get(urlBase)
#Creamos un objeto BS para trabajar con el
docFinal = BeautifulSoup(miDoc.text, "html.parser")

#Devolvemos una lista con las horas(str)
#Realmente esta funcion la podriamos omitir y generar las horas con un for in range
def getHoras():
    lista_horas = []
    for item in docFinal.select('span[itemprop="description"]'):
        print(item)
        lista_horas.append((str(item))[50:59])
    return lista_horas

#Devolvemos una lista con los valores de los precios(str)
def getPrecio():
    lista_precios = []
    for item in docFinal.select('span[itemprop="price"]'):
        result = re.findall("\d+\.\d+", str(item))
        lista_precios.append(result[0])
    return lista_precios

#Devolvemos la media de la lista de precios
def getMedia():
    precios = map(str_to_float,getPrecio())
    return mean(precios)

#Devolvemos num como float
def str_to_float(num):
    return float(num)

#Devolvemos una tupla con los precios que dividen las diferentes tarifas
def precioHorario():
    lista_ordenada = getPrecio()
    lista_ordenada.sort()
    return (float(lista_ordenada[8]),float(lista_ordenada[17]))

def precioValle():
    pass




