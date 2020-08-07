# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:17:25 2020

@author: Fernando
"""

matrix=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],]
for fila in range (0,5):
    for columna in range (0,6):
        print("ingrese los valores i,j: ",fila,columna)
        matrix[fila][columna]=int(input())
print(matrix)