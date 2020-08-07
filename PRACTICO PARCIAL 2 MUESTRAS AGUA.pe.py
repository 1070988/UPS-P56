# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:20:49 2020

@author: Andrés Rodríguez.
"""


print("ANÁLISIS DE MUESTRAS DE AGUA")
a=int(input("Ingrese cantidad de muetsras de agua: "))
while a<=0 or a>=11:
    print("El valor debe ser entre 1 y 10")
    a=int(input("Ingrese cantidad de temperatura [1,10]:"))
l=[]
c=1
for i in range(a):
    print("Temperatura",c, end=" ")
    b=float(input("en °C: "))
    l.append(b)
    c=c+1
d=0
e=0
f=0
for x in range(a):
    if l[x]>=100:
        d=d+1
    if l[x]>0 and l[x]<100:
        e=e+1
    if l[x]<=0:
        f=f+1
for y in range(1):
    g=l[y]
    for z in range(1,a):
        g=g+l[z]
print("\nRESUMEN DEL ANÁLISIS DE MUESTRAS DE AGUA")
print("Cantidad de muestras sólidas: ",d)
print("Cantidad de muestras líquidas: ",e)
print("Cantidad de muestras gaseosas: ",f)
print("\nTemperatura promedio °C: ",g/a)
print("Temperatura promedio °F: ",((g/a)*9/5)+32)