# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:38:20 2020

@author: Andrés Rodríguez.
"""

temp=[]
n =int(input("Ingrese cantidad de muestras que no supere a 10: "))

for i in range (n):
    num=int(input("ingrese la Temperatura en ºC: "))
    temp.append(num)
print(temp)
gaseoso=0
liquido=0
solido=0
for num in temp:
    if (num==100 or num>100) :
        print(num,"Estado Gaseoso", sep="\t")
        gaseoso+=1
    elif (num<0 or num==0):
        print(num, "Estado Sólido", sep="\t")
        solido += 1
    elif (num>0 or num<100):
        print(num, "Estado Liquido", sep="\t")
        liquido += 1

print("RESUMEN DE ANÁLISIS DE MUESTRAS DE AGUA")
print("CANTIDAD DE MUESTRAS EN ESTADO SOLIDO: ", solido)
print("CANTIDAD DE MUESTRAS EN ESTADO LIQUIDO: ", liquido)
print("CANTIDAD DE MUESTRAS EN ESTADO GASEOSO: ", gaseoso)