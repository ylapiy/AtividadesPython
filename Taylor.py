"""

Função exponencial. Suponha que x seja um real positivo. Escreva um programa que calcule e^x usando a expansão da série de Taylor

e^x=1+x+x^2/2!+x^3/3!+x^4/4!+…

"""

numero_entrado = float(input())
import math

contador = 2

resultado = 1 + numero_entrado

while contador < 51:
    elevacao = numero_entrado**contador / math.factorial(contador)
    resultado = resultado + elevacao
    contador = contador + 1

print(resultado)
