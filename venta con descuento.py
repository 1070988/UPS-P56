# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:38:45 2020

@author: Andrés Rodríguez
"""

x=int(input("ingrese la cantidad de llantas que se venderán: "))
y=float(input("ingrese el valor unitario: "))

if x>=4:
    t=x*y
    p=t*0.10
    z=t-p
    print("su compra con el descuento es de: ", z )
else:
    t=x*y
    print("su compra tiene un valor de: ", t)
    



 