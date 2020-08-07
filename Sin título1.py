# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:02:57 2020

@author: Fernando
"""


def isYearLeap(year):
    while True:
        isYearLeap=int(input("ingrese de que año desea obtener informacion"))
        if isYearLeap%4==0:
            if isYearLeap>=1500 or isYearLeap<=2100:
                print("el año: ",isYearLeap," es un año bisiesto")
            else:
                print("el año: ",isYearLeap," no es un año bisiesto")
                
                