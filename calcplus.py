#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == '__main__':
    fichero=open('fichero.txt','r')
    lineas=fichero.readlines()
    calculadora = calcoohija.CalculadoraHija()
    
    #print(lineas)
    for linea in lineas:
        lista= linea[:-1].split(',')
        nuevalista = lista[1:]
        nuevalista = [int(i) for i in nuevalista]   #Convertir el string a int
        
        primernum = nuevalista[0]
        restonum = nuevalista[1:]
        
        
        if lista[0] == "suma":
            resultado=primernum
            for nuevalista in restonum:
                resultado = calculadora.suma(resultado,nuevalista)
            print(resultado)
            
        
        if lista[0] == "resta":
            resultado=primernum
            for nuevalista in restonum:
                resultado = calculadora.resta(resultado,nuevalista)
            print(resultado)        
            
        if lista[0] == "multiplica":
            resultado=primernum
            for nuevalista in restonum:
                resultado = calculadora.multiplicar(resultado,nuevalista)
            print(resultado)
            
        if lista[0] == "divide":
            resultado=primernum
            for nuevalista in restonum:
                resultado =calculadora.dividir(resultado,nuevalista)
            print(resultado)        
 
    fichero.close()
