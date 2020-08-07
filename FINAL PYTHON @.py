# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:13:25 2020

@author: Andrés Rodríguez
"""


def year(bto):
 if bto % 4 == 0:
    if bto % 100 == 0:
        if bto % 400 == 0:
            return True
        else:
            return False
    else:
        return True
 else:
    return False

def estemes(bto , mes):
    if bto<1900 or mes<1 or mes>12:
        return
    
    di = [31,28,31,30,31,30,31,31,30,31,30,31]
    r = di [mes - 1]    
    if mes==2  :
     if year(bto):
       r = 29
    return r

def diaelaño( bto , mes , dia ):
    j=0
    for i in range (1,mes):
        h=estemes(bto, i)
        if h == None:
            return None
        j+=h
    h=estemes(bto , mes)
    if dia >= 1 and dia <= h:
        return j+dia
    else:
        return None

print(diaelaño( 2000, 12, 31 ))


        