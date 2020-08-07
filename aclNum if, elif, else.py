# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:22:05 2020

@author: Fernando
"""


aclnum=int(input("what is the IPv4 ACL number?."))
if aclnum>= 1 and aclnum<=99:
    print("this is a stndard IPv4 ACL.")
elif aclnum>=100 and aclnum<=199:
    print("this a extend IPv4 ACL.")
else:
        print("this is not a standard or extend IPv4 ACL")
        