# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:56:43 2020

@author: Fernando
"""


x=int(input("ingrese el año del cual desea saber si es visiesto o no: "))

if x>=1000 or x<=2100:
    x%4=0
    print("el año ingresado es bisiesto")
else: 
    print("el año no es bisiesto")
    
    
    
    
    		print("desea finalizar el programa (SI) 0 (NO)")
		n = input()
		if n=="SI" or n=="si": break