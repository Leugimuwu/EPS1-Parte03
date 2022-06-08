# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:41:13 2022

@author: alumno
"""

def error(): 
    print("Opcion incorrecta")
    
def salir():
    print("Gracias... Vuelva pronto")
    
def agregar():
    
    dni_agre = open("dni.txt","at")
    nombre_agre = open("nombre.txt","at")
    apellido_agre = open("apellido.txt","at")
    
    dni_agre.write(input("Ingrese dni : ")+"\n")
    dni_agre.close()
    
    nombre_agre.write(input("Ingrese nombre : ")+"\n")
    nombre_agre.close()
    
    apellido_agre.write(input("Ingrese apellido : ")+"\n")
    apellido_agre.close()
    
    
def listar():
    #SEPARAR CADENA
    dni = open("dni.txt","rt",encoding="utf8")
    lista_dni = dni.read().split("\n")
    
    nombre = open("nombre.txt","rt",encoding="utf8")
    lista_nombre = nombre.read().split("\n")
    
    apellido = open("apellido.txt","rt",encoding ="utf8")
    lista_apellido = apellido.read().split("\n")
    
    i=0
    print("DNI   |  NOMBRE  |   APELLIDO")
    for i in range(0,len(lista_dni)-1):
        print(lista_dni[i]+" | "+lista_nombre[i]+" | "+lista_apellido[i])