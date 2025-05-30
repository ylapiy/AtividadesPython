"""

Escreva um programa que lê um número inteiro n e imprime a sequência Thue-Morse de ordem n.

As primeiras cadeias de caracteres são 0, 01, 0110, 01101001.

Cada cadeia sucessiva é obtida invertendo todos os bits da cadeia anterior e concatenando o resultado ao final da cadeia anterior.

A sequência tem muitas propriedades surpreendentes. Por exemplo, é uma sequência binária livre de cubos: não contém 000, 111, 010101 ou sss, onde s é qualquer cadeia de caracteres. Ela é autossimilar: se você excluir todos os outros bits, obterá outra sequência de Thue-Morse. Ela surge em diversas áreas da matemática, bem como no xadrez, no design gráfico, nos padrões de tecelagem e na composição musical.

"""


def ThueMorse(n):
    sequencia = "0"
    for _ in range(n):
        inverso = ""
        for caracteres in sequencia:
            if caracteres == "0":
                inverso = inverso + "1"
            elif caracteres == "1":
                inverso = inverso + "0"
        sequencia = sequencia + inverso
    print(sequencia)


Entrada = int(input())


ThueMorse(Entrada)
