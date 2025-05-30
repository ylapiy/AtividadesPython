"""
Em 1693, Samuel Pepys perguntou a Isaac Newton o que era mais provável: obter pelo menos um 1 ao lançar um dado justo 6 vezes ou obter pelo menos dois 1s ao lançar um dado justo 12 vezes. Escreva um programa que use simulação para determinar a resposta correta.

O programa deve ler três números inteiros p, q e s (separados por <espaço>), onde p é a quantidade de observações da face 1, q é a quantidade de repetições e s é uma semente (seed) para auxiliar na reprodutibilidade.

O programa deve repetir o seguinte experimento q vezes:

Rolar o dado 6*p vezes
Contar a quantidade de 1
Sucesso = pelo menos p 1s
A saída deve ser a probabilidade de sucesso em q tentativas.

NOTE que o input deve ser: p<espaço>q<espaço>s
"""

import random

p, q, s = map(int, input().split())

random.seed(s)

sucessosd1 = 0
sucessosd2 = 0

for i in range(q):
    rolagens = random.choices(range(1, 7), k=6 * p)
    if rolagens.count(1) >= p:
        sucessosd1 = sucessosd1 + 1

for i in range(q):
    rolagens = random.choices(range(1, 7), k=6 * p * 2)
    if rolagens.count(1) >= p * 2:
        sucessosd2 = sucessosd2 + 1

probabilidade1 = sucessosd1 / q
probabilidade2 = sucessosd2 / q

if probabilidade1 > probabilidade2:
    print(probabilidade1)
elif probabilidade2 > probabilidade1:
    print(probabilidade2)
