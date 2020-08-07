# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:03:49 2020

@author: Fernando
"""


x=int(input("ingrese los valores a los cuales quiere contar: "))
contador=1
acumulador=0
while True:
    print(contador)
    contador+=1
    if contador > x:
        break