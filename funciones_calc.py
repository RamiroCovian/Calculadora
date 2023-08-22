# Funciones de la calculadora


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multi(a, b):
    return a * b


def divi(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre 0")
    return a / b


def porcent(a, b):
    return (a * b) / 100
