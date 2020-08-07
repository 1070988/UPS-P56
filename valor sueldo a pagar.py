# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:31:11 2020

@author: Andrés Rodríguez
"""

h=int(input("ingrese la cantidad de horas trabajadas: "))
t=int(input("ingrese el valor pagado de la tarifa por hora: "))
d=int(input("ingrese el descuento: "))
if h>=40:
    x=h-40
    y=t*40-d
    u=x*t
    m=u*0.5
    r=y+u+m
    print("valor total a pagar: ",r )
else:
    w=h*t-d
    print("el valor a pagar es: ", w)
    