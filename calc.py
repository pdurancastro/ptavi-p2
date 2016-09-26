#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def plus(op1, op2):
    """ Function to sum the operands """
    return op1+op2


def minus(op1, op2):
    """ Function to substract the operands """
    return op1-op2


def mult(op1, op2):
    return op1*op2


def div(op1, op2):
    try:
        return op1/op2
    except ZeroDivisionError:
        sys.exit("Error:No puedes dividir un numero 0")


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: No es un parametro numerico")

    if sys.argv[2] == "suma":
        result = plus(operando1, operando2)

    elif sys.argv[2] == "resta":
        result = minus(operando1, operando2)

    elif sys.argv[2] == "multiplicar":
        result = mult(operando1, operando2)

    elif sys.argv[2] == "dividir":
        result = div(operando1, operando2)

    else:
        sys.exit('Operación no valida.')

    print(result)
