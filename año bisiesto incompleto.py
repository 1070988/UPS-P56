# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:10:52 2020

@author: Andrés Rodríguez
"""

def estemes(mes):
 if mes<1 or mes>12:
     return
di = [31,28,31,30,31,30,31,31,30,31,30,31]
  rest = di [mes-1]    
  if mes == 2:
    rest == 29
  return rest

print(estemes(2))