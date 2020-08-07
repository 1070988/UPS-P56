# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:18:24 2020

@author: Andres Rodriguez
"""

import numpy as np
from random import randint
print("ingrese el numero de filas que desea para su matriz: ")
rows=int(input())    
print("ingrese el numero de columnas que desea para su matriz: ")
columns=int(input())
print("\n"*0)
matrix=np.zeros([rows,columns])
f=-1
c=-1
a=rows
b=rows
for i in range(0,rows):
    for n in range(0,columns):
        matrix[i][n]=int(randint(0,99))
print("su matriz es de: ",rows,"x",columns)
print("\n"*0)
print(matrix)
print("\n"*0)
print('El valor de la diagonal principal de la matriz es: ')
print("\n"*0)
for j in range(0,rows):
    if f<rows:
        f+=1
        a-=1
    print(' | -- |'*f,"|",int(matrix[j][f]),"|",'| 0 | '*a)
    
print('\nEl valor de la diagonal secundaria de la matriz es: ')
print("\n"*0)
for k in range(0,rows):
    if c<rows:
        c+=1
        b-=1
    print(' | -- |'*b,"|",int(matrix[k][b]),"|",'| 0 | '*c)

