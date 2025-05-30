"""

Escreva um programa que lê um número inteiro N e imprime um padrão gravata borboleta (2N+1) por (2N+1), como o apresentado a seguir:


* . . . . . *

* * . . . * *

* * * . * * *

* * * * * * *

* * * . * * *

* * . . . * *


* . . . . . *


NOTE que os caracteres estão separados por <espaço>, ou seja:

*<espaço>.<espaço>.<espaço>.<espaço>.<espaço>.<espaço>*<espaço>

*<espaço>*<espaço>.<espaço>.<espaço>.<espaço>*<espaço>*<espaço>

*<espaço>*<espaço>*<espaço>.<espaço>*<espaço>*<espaço>*<espaço>

*<espaço>*<espaço>*<espaço>*<espaço>*<espaço>*<espaço>*<espaço>

*<espaço>*<espaço>*<espaço>.<espaço>*<espaço>*<espaço>*<espaço>

*<espaço>*<espaço>.<espaço>.<espaço>.<espaço>*<espaço>*<espaço>


*<espaço>.<espaço>.<espaço>.<espaço>.<espaço>.<espaço>*<espaço>

"""


def Borboleta(Entrada):
    Inteiro = Entrada * 2 + 1
    meio = Inteiro // 2
    contador = 1
    matriz = [["* " for _ in range(Inteiro)] for _ in range(Inteiro)]

    for i in range(Inteiro):
        for e in range(contador, Inteiro - contador):
            matriz[i][e] = ". "

        if i < meio:
            contador = contador + 1
        elif i >= meio:
            contador = contador - 1

    for linha in matriz:
        print("".join(linha))


Entrada = int(input())

Borboleta(Entrada)
