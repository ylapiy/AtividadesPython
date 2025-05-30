"""
Funções trigonométricas. Escreva um programa que calcula sen(x) usando as expansões da série de Taylor

sen(x)=x−x^3/3!+x^5/5!−x^7/7!+…
"""

numero_entrado = float(input())
import math

contador_valores = 3
contador_par_impar = 1

resultado = numero_entrado

while contador_valores < 100:
    if contador_valores % 2 != 0:
        elevacao = numero_entrado**contador_valores / math.factorial(contador_valores)
        if contador_par_impar % 2 != 0:
            resultado = resultado - elevacao

        else:
            resultado = resultado + elevacao

        contador_par_impar = contador_par_impar + 1
    contador_valores = contador_valores + 1

print(resultado)
