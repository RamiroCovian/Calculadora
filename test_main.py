# Test de las funciones basicas

from funciones_calc import sumar, resta, multi, divi, porcent

print(sumar(2, 4))  # 6
print(sumar(4, 2))  # 6
print(resta(4, 2))  # 2
print(resta(2, 4))  # -2
print(multi(4, 2))  # 8
print(multi(2, 4))  # 8
print(divi(4, 2))  # 2
print(divi(2, 4))  # 0.5
print(porcent(4, 2))  # 0.08
print(porcent(2, 4))  # 0.08
print(porcent(2, 0))  # 0
print(porcent(0, 2))  # 0
print(divi(9, 0))  # ERROR
