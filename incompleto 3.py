# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:56:32 2020

@author: Fernando
"""


while True:
		x=int(input("ingrese el año para determinar si es bisiesto o no: "))
		if x%4=0:
			if x>1500:
				print("el año: ",x"es un año bisiesto")
		else:
			print("el año: ",isYearLeap," no es un año bisiesto")
		print("desea finalizar el programa (SI) 0 (NO)")
		n = input()
		if n=="SI" or n=="si": break
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
    result=isYearLeap(yr)
if result == testResults[i]:
		print("OK")
else:
		print("Failed")
