#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys



if __name__ == '__main__':
    fichero=open('fichero.txt','r')
    lineas=fichero.readlines()
    
    #print(lineas)
    for linea in lineas:
        lista= linea[:-1].split(',')
        if lista[0] == "suma":                       
            nuevalista = lista[1:]
            nuevalista = [int(i) for i in nuevalista]   #Convertir el string a int
            suma=0
            for i in nuevalista:
               suma += i
            print(suma)
               
        if lista[0] == "resta":       
               
                
            
            print(nuevalista)
            #for i in nuevalista:
                #nuevalistastring += i
                #print(nuevalistastring)                
            #resultado= int(lista[n]) + int(lista[n+1])
       
        #print(lista)
       
    #print(fichero.read())

    fichero.close()
