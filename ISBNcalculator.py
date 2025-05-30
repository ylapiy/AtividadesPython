"""

O International Standard Book Number (ISBN) é um código de 10 dígitos que especifica exclusivamente um livro. O dígito mais à direita é um dígito de soma de verificação que pode ser determinado exclusivamente a partir dos outros 9 dígitos, com base na condição de que:

d_1 + 2d_2 + 3d_3 + ... + 10d_10

deve ser um múltiplo de 11 (aqui d_i denota o i-ésimo dígito da direita).

O dígito da soma de verificação d_1 pode ser qualquer valor de 0 a 10: a convenção do ISBN é usar o valor X para indicar 10.

Exemplo: o dígito da soma de verificação correspondente a 020131452 é 5, pois é o único valor de d_1 entre 0 e 10 para o qual d1 + 2*2 + 3*5 + 4*4 + 5*1 + 6*3 + 7*1 + 8*0 + 9*2 + 10*0 é um múltiplo de 11.

Escreva um programa que lê um número inteiro de 9 dígitos, calcula a soma de verificação e imprime o número ISBN de 10 dígitos.

Obs: se houver zeros à esquerda, Imprima.

"""

codigo_a_ser_verificado = input().strip()
d10 = 0

if len(codigo_a_ser_verificado) != 9:
    print("Número ISBN inválido")
else:
    soma = sum(int(codigo_a_ser_verificado[i]) * (i + 1) for i in range(9))

    while (soma + (d10 * 10)) % 11 != 0 and d10 < 10:
        d10 += 1

    isbn_valido = codigo_a_ser_verificado + str(d10)
    print(isbn_valido)
