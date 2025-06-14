"""
Escreva um programa que lê um inteiro positivo N e imprime uma matriz N por N que começa com 1 no centro, vai para a direita e segue aumentando em espiral, conforme mostrado nos exemplos a seguir:

N = 3

7 8 9

6 1 2

5 4 3


N = 4

7  8  9 10

6  1  2 11

5  4  3 12

16 15 14 13


NOTE que os números estão separados por <espaço>, ou seja:

7<espaço>8<espaço>9

6<espaço>1<espaço>2

5<espaço>4<espaço>3


"""


def MatrizEspiral(N):
    if N % 2 == 1:
        meio = N // 2
    else:
        meio = N // 2 - 1

    contadorNumeros = 2
    ContadorRotacoes = 1
    linha = meio
    coluna = meio

    matriz = [["0" for _ in range(N)] for _ in range(N)]
    matriz[linha][coluna] = "1"

    direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0

    while contadorNumeros <= N * N:
        for _ in range(2):
            mundancaLinha, mudancaColuna = direcoes[dir_idx % 4]
            for _ in range(ContadorRotacoes):
                linha += mundancaLinha
                coluna += mudancaColuna
                if 0 <= linha < N and 0 <= coluna < N:
                    matriz[linha][coluna] = str(contadorNumeros)
                    contadorNumeros += 1
            dir_idx += 1
        ContadorRotacoes += 1

    for linha in matriz:
        print(" ".join(linha))


Entrada = int(input())
MatrizEspiral(Entrada)
