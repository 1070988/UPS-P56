# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:19:23 2020

@author: Fernando
"""
apellido=input("introduce tu apellido: ")
nombre=input("introduce tu nombre: ")
edad=int(input("ingresa tu edad que sea menos a 100 años: "))
if edad>=1 and edad<=9:
    print("usted aun es un niño")
elif edad >=10 and edad <=18:
    print("usted aun es un adolecente")
elif  edad>=19 and edad<=40:
    print("usted aun es joven")
elif edad>=41 and edad<=60:
    print("usted aun es un adulto")
else:
    print("ustd es un adulto mayor")
ubicacion=input("introduce tu ubicacion: ")
print(type)
print("hola a todos, to soy ", apellido, nombre, "tengo ", edad, "años, y actualmente vivo en ", ubicacion, "y", edad)