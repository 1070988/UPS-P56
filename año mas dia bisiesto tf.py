# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:53:32 2020

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

print(estemes( 2020 , 2 ))
    
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 3, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	y = testYears[i]
	m = testMonths[i]
	print(y, m, "->", end="")
	result = estemes(y, m)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
