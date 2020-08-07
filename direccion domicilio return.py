# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:40:52 2020

@author: Andrés Rodríguez
"""


def direccion(calle,sector,codigopostal,referencia,numcasa):
    print("su direccion esta en: el sector: ",sector,"y su calle es: ",calle)
    print("el numero de su casa es: ",numcasa,"con codigo postal: ",codigopostal)
    print("cerca de: ", referencia)
    
print("ingrese los datos que se necesitan para ubicar su domicilio.")
calle=input("ingrese la calle en la cual esta su domicilio: ")
sector=input("ingrese el sector en el cual esta su domicilio: ")
codigopostal=input("ingrese su codigo postal: ")
referencia=input("de una referencia cercana a su domicilio: ")
numcasa=input("digite cual es su numero de casa: ")

direccion(calle,sector,codigopostal,referencia,numcasa)