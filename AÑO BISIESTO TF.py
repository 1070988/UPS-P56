# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:21:01 2020

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
x=year(2020)
print(x)

testData = [1900, 2020, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = year(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")