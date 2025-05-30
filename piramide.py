"""

Escreva um programa que lê um número inteiro N e imprime um padrão triangular N por N, como o apresentado a seguir:

* * *

. * *

. . *

NOTE que os caracteres estão separados por <espaço>, ou seja:
*<espaço>*<espaço>*<espaço>

.<espaço>*<espaço>*<espaço>

.<espaço>.<espaço>*<espaço>
"""


def Piramide(Inteiro):
    sequenciafila = ""
    contador_de_pontos = 0
    matriz = [["* " for _ in range(Inteiro)] for _ in range(Inteiro)]

    for i in range(Inteiro):
        sequenciafila = ""
        for e in range(contador_de_pontos):
            if contador_de_pontos < 0:
                continue
            if contador_de_pontos > -1:
                matriz[i][e] = ". "
        contador_de_pontos = contador_de_pontos + 1

    for linha in matriz:
        print("".join(linha))


Entrada = int(input())

Piramide(Entrada)
