# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:12:53 2020

@author: Andrés Rodríguez
"""

x=int(input("ingrese hasta que numero quiere contar: "))
y=1
while True:
    x=float(x) 
    if x == "q" or x=="QUIT":
        break
    else:
        while True:
    print(y)
    y=y+1
    if y > x:
        break
    
    
        
