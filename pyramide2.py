"""
Escreva um programa que lê um número inteiro N e imprime um padrão triangular N por N, como o apresentado a seguir:

. . . * . . .

. . * * * . .

. * * * * * .

* * * * * * *

. * * * * * .

. . * * * . .


. . . * . . .


NOTE que os caracteres estão separados por <espaço>, ou seja:

.<espaço>.<espaço>.<espaço>*<espaço>.<espaço>.<espaço>.<espaço>

.<espaço>.<espaço>*<espaço>*<espaço>*<espaço>.<espaço>.<espaço>

.<espaço>*<espaço>*<espaço>*<espaço>*<espaço>*<espaço>.<espaço>

*<espaço>*<espaço>*<espaço>*<espaço>*<espaço>*<espaço>*<espaço>

.<espaço>*<espaço>*<espaço>*<espaço>*<espaço>*<espaço>.<espaço>

.<espaço>.<espaço>*<espaço>*<espaço>*<espaço>.<espaço>.<espaço>


.<espaço>.<espaço>.<espaço>*<espaço>.<espaço>.<espaço>.<espaço>

"""


def Piramide(Entrada):
    Inteiro = Entrada * 2 + 1
    meio = Inteiro // 2
    contadorInicio = Inteiro // 2
    contadorFim = Inteiro // 2 + 1
    matriz = [[". " for _ in range(Inteiro)] for _ in range(Inteiro)]

    for i in range(Inteiro):
        for e in range(contadorInicio, contadorFim):
            matriz[i][e] = "* "

        if i < meio:
            contadorInicio = contadorInicio - 1
            contadorFim = contadorFim + 1
        if i >= meio:
            contadorInicio = contadorInicio + 1
            contadorFim = contadorFim - 1

    for linha in matriz:
        print("".join(linha))


input = int(input())
Piramide(input)
