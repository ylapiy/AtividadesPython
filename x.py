"""
Escreva um programa que lê um número inteiro N e imprime um “X” (2N+1) por (2N+1), como o apresentado a seguir:

* . . . . . *

. * . . . * .

. . * . * . .

. . . * . . .

. . * . * . .

. * . . . * .

* . . . . . *

NOTE que os caracteres estão separados por <espaço>, ou seja


*<espaço>.<espaço>.<espaço>.<espaço>.<espaço>.<espaço>*<espaço>

.<espaço>*<espaço>.<espaço>.<espaço>.<espaço>*<espaço>.<espaço>

.<espaço>.<espaço>*<espaço>.<espaço>*<espaço>.<espaço>.<espaço>

.<espaço>.<espaço>.<espaço>*<espaço>.<espaço>.<espaço>.<espaço>

.<espaço>.<espaço>*<espaço>.<espaço>*<espaço>.<espaço>.<espaço>

.<espaço>*<espaço>.<espaço>.<espaço>.<espaço>*<espaço>.<espaço>

*<espaço>.<espaço>.<espaço>.<espaço>.<espaço>.<espaço>*<espaço>
"""


def X(Inteiro):
    tamanho = 2 * Inteiro + 1
    matriz = [["" for _ in range(tamanho)] for _ in range(tamanho)]

    for i in range(tamanho):
        sequencia = ""
        for e in range(tamanho):
            matriz[i][e] = ". "
            if i == e:
                matriz[i][e] = "* "
            if i + e == tamanho - 1:
                matriz[i][e] = "* "
            sequencia = sequencia + matriz[i][e]
        print(sequencia)


Entrada = int(input())
X(Entrada)
