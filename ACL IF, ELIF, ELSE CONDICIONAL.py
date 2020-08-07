# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:18:10 2020

@author: Andrés
"""

acl=input("ingrese el numero de ACL !!"+"/n : "  )
acl=int(acl)
print("/n"*2)
if acl>=1 and acl<=99:
    print("es ACL STANDARD")
elif acl>=100 and acl<=199:
    print("es ACL EXTENDIDA")
else:
    print("no es ACL")
