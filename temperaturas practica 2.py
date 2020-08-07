# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:17:46 2020

@author: Fernando
"""


x=float(input("INGRESE LA CANTIDAD DE MUESTRAS QUE DESEA INGRESAR: "))
if x==0 or x>=10:
    print("la cantidad de muestras superan el limite. ")
elif x==1:
    print("la cantidad de muestras ingresasadas es: ",x)
    q=float(input("ingrese la temperatura del agua en grados ºC: "))
    if q<=0:
        print("el estado de la muestra es solido.")
    elif q>0 and q <100:
        print("la muestra del agua esta en estado liquido.")
    elif q>=100:
        print("la muestra esta en estado gaseoso.")
    print("la temperatura promedio en grados ºC es: ",q)
    w=(q*1.8)+32
    print("la temperatura promedio en grados ºF es: ",w)
elif x==2:
    print("la cantidad de muestras ingresasadas es: ",x)
    e=float(input("ingrese la temperatura del agua en grados ºC de la muestra 1: "))
    r=float(input("ingrese la temperatura del agua en grados ºC de la muestra 2: "))
    if e<=0:
        print("el estado de la muestra es solido.")
    elif e>0 and e<100:
        print("la muestra del agua esta en estado liquido.")
    elif e>=100:
        print("la muestra esta en estado gaseoso.")
    print("la temperatura promedio en grados ºC es: ",e)
    t=(e*1.8)+32
    print("la temperatura promedio en grados ºF es: ",t)
    if t<=0:
        print("el estado de la muestra es solido.")
    elif t>0 and t<100:
        print("la muestra del agua esta en estado liquido.")
    elif t>=100:
        print("la muestra esta en estado gaseoso.")
    u=(e+r)%2
    print("la temperatura promedio en grados ºC es: ",u)
    y=(t*1.8)+32
    i=(t+y)%2
    print("la temperatura promedio en grados ºF es: ",i)
        
    