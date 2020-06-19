# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:14:30 2020

@author: Andrés
"""

ipadd={"R1":"10.0.0.1","R2":"10.00.2","R3":"10.0.0.3","S1":"10.1.0.1","S2":"10.1.0.2"}

print(type(ipadd))

dict1={"usuario":"1070988184","valor":5000,"edad":21,"soltero":True,"rate en %":25.2}

print(ipadd["S2"])

ipadd["S4"]="10.1.1.10"

print("S1" in  ipadd)

print(5000 in ipadd)