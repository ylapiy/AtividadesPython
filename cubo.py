"""
S. Ramanujan foi um matemático indiano que ficou famoso por sua intuição com os números.

Um dia, quando o matemático inglês G. H. Hardy foi visitá-lo no hospital, Hardy observou que o número de seu táxi era 1729, um número um tanto sem graça.

Ao que Ramanujan respondeu: “Não, Hardy! Não, Hardy! É um número muito interessante. É o menor número que pode ser expresso como a soma de dois cubos de duas maneiras diferentes.”

Verifique essa afirmação escrevendo um programa que lê um inteiro n e imprime TODOS os números inteiros menores ou iguais a n que podem ser expressos como a soma de dois cubos de PELO MENOS DUAS maneiras diferentes - encontre números inteiros positivos distintos a, b, c e d de modo que a^3 + b^3 = c^3 + d^3.

NOTE que você deve imprimir os <espaços> entre os números =  a^3<espaço>+<espaço>b^3<espaço>=<espaço>c^3<espaço>+<espaço>d^3

Imprimir as saídas ordenadas pelo valor da SOMA, conforme observado no exemplo abaixo.

"""
numero = int(input())
limite = int(numero ** (1 / 3))
numeros_ja_impresos = []

for i in range(limite):
    for e in range(limite):
        for d in range(limite):
            for f in range(limite):
                esquerda = (i**3) + (e**3)
                direita = (d**3) + (f**3)
                if (
                    (i**3) + (e**3) == (d**3) + (f**3)
                    and i != e
                    and i != d
                    and i != f
                    and d != e
                    and d != i
                    and d != f
                    and f != e
                    and f != d
                    and f != i
                ):
                    if esquerda not in numeros_ja_impresos:
                        numeros_ja_impresos.append(esquerda)
                        impresão = f"{esquerda} = {i}^{3} + {e}^{3} = {d}^{3} + {f}^{3}"
                        print(impresão)
