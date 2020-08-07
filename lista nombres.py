# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:56:31 2020

@author: Fernando
"""



auxiliar=str()
vector=[str() for indo in range (28)]
tamvector=(int(input("ingrese el tamaño del vector: ")))
for i in range (1, tamvector+1):
    vector[i-1]=str(str)
    print("el valor en la psoicion ",i," es ",vector[i-1])
    sleep(1)
sleep(1)
for j in range (1, tamvector+1):
    for l in range (1, tamvector+1):
        if vector[l-1]<vector[l]:
            auxiliar=vector[l-1]
            vector[l-1]=vector[l]
            vector[l]=auxiliar
for k in range (1, tamvector+1):
    print("el vector ordenado en la posision: ",k, " es ",vector[k-1])
    sleep(1)