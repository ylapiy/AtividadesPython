"""

O Código Universal de Produto (UPC) é um código de 12 dígitos que especifica exclusivamente um produto.

O dígito menos significativo, d_1 (o mais à direita), é um dígito de verificação que é determinado exclusivamente ao tornar a seguinte expressão um múltiplo de 10:

(d_1 + d_3 + d_5 + d_7 + d_9 + d_11) + 3 (d_2 + d_4 + d_6 + d_8 + d_10 + d_12)

Por exemplo, o dígito verificador correspondente a 0-48500-00102 (Tropicana Pure Premium Orange Juice) é 8, pois (8 + 0 + 0 + 0 + 5 + 4) + 3 (2 + 1 + 0 + 0 + 8 + 0) = 50 e 50 é um múltiplo de 10.

"""

codigo_a_ser_verificado = input().strip()
d1 = 0

if len(codigo_a_ser_verificado) != 11:
    print("Número UPC inválido")
else:
    int(codigo_a_ser_verificado)

    while (
        sum(
            [
                d1,
                int(codigo_a_ser_verificado[9]),
                int(codigo_a_ser_verificado[7]),
                int(codigo_a_ser_verificado[5]),
                int(codigo_a_ser_verificado[3]),
                int(codigo_a_ser_verificado[1]),
            ]
        )
        + 3
        * sum(
            [
                int(codigo_a_ser_verificado[10]),
                int(codigo_a_ser_verificado[8]),
                int(codigo_a_ser_verificado[6]),
                int(codigo_a_ser_verificado[4]),
                int(codigo_a_ser_verificado[2]),
                int(codigo_a_ser_verificado[0]),
            ]
        )
    ) % 10 != 0 and d1 < 10:
        d1 += 1

    UPC_valido = codigo_a_ser_verificado + str(d1)
    print(UPC_valido)
