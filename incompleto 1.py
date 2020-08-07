"""
Created on Tue Jul  7 12:44:55 2020

@author: Andrés Rodríguez
"""

x=int(input("ingrese el año del cual desea saber si es visiesto o no: "))

if x>=1000 or x<=2100:
    x%4=0
    print("el año ingresado es bisiesto")
else: 
    print("el año no es bisiesto")