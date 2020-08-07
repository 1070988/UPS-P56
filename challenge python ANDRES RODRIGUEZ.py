# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:44:18 2020

@author: Andrés Rodríguez
"""



print("Ingrese el tamaño vector: ")
tamañovector=int(input())
if tamañovector>=3:
    print("Desea trabajar con numeros o caracteres?")
    op=str(input())
    if op=="caracteres":
        auxiliaru=str()
        nombre=str()
        vectoru=[str() for ind0 in range(100)]
        for i in range(1,tamañovector+1):
            print("Ingrese el/los caracteres: ",i)
            nombre=input()
            vectoru[i-1]=nombre
            print("El valor de la posicion",i,"es",vectoru[i-1])
        print("Si desea ordenar de menor a mayor digite 1, si desea de mayor a menor digite 2 ")
        orden=int(input())
        if orden==1:
            for j in range(1,tamañovector+1):
                for l in range(1,tamañovector+1):
                    if vectoru[l-1]>vectoru[l]:                        
                        auxiliaru=vectoru[l-1]
                        vectoru[l-1]=vectoru[l]
                        vectoru[l]=auxiliaru
            for k in range(1,tamañovector+1):
                print("El vector ordenado en la posicion",k,"es",vectoru[k-1])
        if orden==2:
            for j in range(1,tamañovector+1):
                for l in range(1,tamañovector+1):
                    if vectoru[l-1]<vectoru[l]:
                        auxiliaru=vectoru[l-1]
                        vectoru[l-1]=vectoru[l]
                        vectoru[l]=auxiliaru
            for k in range(1,tamañovector+1):
                print("El vector ordenado en la posicion",k,"es",vectoru[k-1])
    if op=="numeros":
        from random import randint
        from time import sleep
        auxiliar=int()
        vector=[int() for ind0 in range(100)]
        print("Ingrese tamaño vector")
        tamanovector=int(input())
        for i in range(1,tamanovector+1):
            vector[i-1]= randint(0,99)
            print("El valor de la posicion",i,"es",vector[i-1])
            sleep(1)
        sleep(1)
        print("Si desea ordenar de menor a mayor digite 1, si desea de mayor a menor digite 2 ")
        orden=int(input())
        if orden==1:
            for j in range(1,tamanovector+1):
                for l in range(1,tamanovector+1):
                    if vector[l-1]>vector[l]:
                        auxiliar=vector[l-1]
                        vector[l-1]=vector[l]
                        vector[l]=auxiliar
            for k in range(1,tamanovector+1):
                print("El vector ordenado en la posicion",k,"es",vector[k-1])
                sleep(1)
        if orden==2:
            for j in range(1,tamanovector+1):
                for l in range(1,tamanovector+1):
                    if vector[l-1]<vector[l]:
                        auxiliar=vector[l-1]
                        vector[l-1]=vector[l]
                        vector[l]=auxiliar
            for k in range(1,tamanovector+1):
                print("El vector ordenado en la posicion",k,"es",vector[k-1])
                sleep(1)
                

           
    