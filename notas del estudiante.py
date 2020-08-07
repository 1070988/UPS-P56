# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:59:16 2020

@author: Andrés Rodríguez
"""


x=int(input("ingrese la primer nota: "))
y=int(input("ingrese la segunda nota: "))
z=int(input("ingrese la tercer nota: "))
if x<=y and x<=z:
    r=y+z
    print("la nota mas alta del estudiante es: ",r)
elif y<=x and y<=z:
    q=x+z
    print("la nota mas alta del estudiante es: ",q)
elif z<=x and z<=y:
    l=x+y
    print("la nota mas alta del estudiante es: ",l)
    
    