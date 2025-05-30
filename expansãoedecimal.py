"""
Dados dois números inteiros p e q, a expansão decimal de p/q tem um ciclo de repetição infinita.

Por exemplo, 1/33 = 0,03030303....

Usamos a notação 0.(03) para indicar que 03 se repete indefinidamente.

Como outro exemplo, 8639/70000 = 0,1234(142857).

Escreva um programa que lê dois números inteiros p e q (separados por <espaço>) e imprime a expansão decimal de p/q usando a notação acima.

"""

p, q = map(int, input().split())


def Expansao(p, q):
    parte_inteira = p // q
    resto = p % q
    listaDeRestos = {}
    listaDeDecimais = []
    inicio_periodico = None

    while resto not in listaDeRestos and resto != 0:
        listaDeRestos[resto] = len(listaDeDecimais)
        resto *= 10
        digito = resto // q
        listaDeDecimais.append(digito)
        resto %= q

        if resto in listaDeRestos:
            inicio_periodico = listaDeRestos[resto]
            break

    if inicio_periodico is None:
        parte_decimal = "".join(str(d) for d in listaDeDecimais)
        print(f"{parte_inteira}.{parte_decimal}")
    else:
        parte_nao_periodica = "".join(
            str(d) for d in listaDeDecimais[:inicio_periodico]
        )
        parte_periodica = "".join(str(d) for d in listaDeDecimais[inicio_periodico:])
        print(f"{parte_inteira}.{parte_nao_periodica}({parte_periodica})")


Expansao(p, q)
