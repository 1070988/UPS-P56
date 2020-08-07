# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 18:36:07 2020

@author: Andrés Rodríguez
"""
#No serán años bisiestos los que sean múltiplos de 100, excepto si también lo son de 400
print("No serán años bisiestos los que sean múltiplos de 100, excepto si también lo son de 400")
def year(bto):
 if bto>=1300 or bto<=2200:
  if bto%4!=0:
      return False
  elif bto%100!=0:
      return True
  elif bto%400!=0:
     return False
  else:
      return True
      return False
x=year(1800)
print(x)
 
testData = [1900, 2012, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = year(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

