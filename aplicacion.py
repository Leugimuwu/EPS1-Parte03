# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:07:44 2022

@author: alumno
"""
 
def login(usuario, contraseña):
    us = open("login.txt","rt",encoding='utf8')
    datos_us = us.read()
    
    con = open("clave.txt","rt",encoding='utf8')
    datos_con = con.read()
    
    if usuario == datos_us and contraseña == datos_con:
        return 1
    return 0

def menu():
    print("======MENU PRINCIPAL======")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")

def principal():
    opcion = 1
    while opcion!=3:
        menu()
        opcion = int(input("Seleccione una opción [1-3]: "))
        print("=========================")
        if opcion ==1:
            print("En proceso")
        elif opcion == 2:
            print("En proceso")
        elif opcion == 3:
            print("En proceso")
        else:
            print("En proceso")

i = 1
while i <= 2:
    if 1 == login(input("Usuario: "),input("Contraseña: ")):
        print("INGRESO CORRECTO")
        principal()
        i=3
        
    else:
        print("incorrecto")
    i += 1
