# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:44:32 2020

@author: Fernando
"""


valor=input("ingrese el limite de veces que quiere contarlo: ")
valor=int(valor)
contador=1
acumulador=0
while contador<=valor:
    print(contador, end=" ")
    acumulador+=contador
    contador+=1
print("la suma de todos los tados es : ", acumulador)
print("el promedio total es: ", acumulador/valor)
    