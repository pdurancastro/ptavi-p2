#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

if __name__ == '__main__':
    calculadora = calcoohija.CalculadoraHija()

    with open('fichero.txt') as csvfile:
        calcreader = csv.reader(csvfile)
        for calcreader in calcreader:
            nuevalista = calcreader[1:]
            nuevalista = [int(i) for i in nuevalista]
            primernum = nuevalista[0]
            restonum = nuevalista[1:]
            if calcreader[0] == "suma":
                resultado = primernum
                for nuevalista in restonum:
                    resultado = calculadora.suma(resultado, nuevalista)
                print(resultado)
            if calcreader[0] == "resta":
                resultado = primernum
                for nuevalista in restonum:
                    resultado = calculadora.resta(resultado, nuevalista)
                print(resultado)
            if calcreader[0] == "multiplica":
                resultado = primernum
                for nuevalista in restonum:
                    resultado = calculadora.multiplicar(resultado, nuevalista)
                print(resultado)
            if calcreader[0] == "divide":
                resultado = primernum
                for nuevalista in restonum:
                    resultado = calculadora.dividir(resultado, nuevalista)
                print(resultado)
