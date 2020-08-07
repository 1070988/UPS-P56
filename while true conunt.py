# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:24:54 2020

@author: Andrés Rodríguez
"""


while True:
    x=input("ingrese el numero a conntar hasta: ")
        
    if x=="q" or x=="quit":
        break
    x=int(x)
    y=1
    
    while True:
        print(y)
        y=y+1
        if y>x:
            break