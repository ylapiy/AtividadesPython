"""'
Um grupo de N amigos decide promover um amigo secreto. Para isso, eles usam um gerador de permutações aleatórias dos números 0, 1, …, N−1. A regra do jogo é a seguinte:

A pessoa 0 dá seu presente para a pessoa a[0] (onde a[] é a permutação gerada);
Em seguida, a pessoa a[0] dá seu presente para a[a[0]];
E assim por diante, seguindo o encadeamento da permutação;
Quando uma pessoa que já participou do ciclo é reencontrada, o processo para e, caso ainda existam pessoas que não deram seus presentes, uma delas é escolhida arbitrariamente para iniciar um novo ciclo.
Dizemos que ocorreu o fenômeno S (de "surpreendente") quando todo o grupo está envolvido em um único ciclo e esse ciclo começa pela pessoa 0 e termina nela mesma, ou seja, todos os amigos deram e receberam presentes dentro do mesmo ciclo iniciado por 0.



Você deve escrever um programa que estime a probabilidade p_N desse fenômeno ocorrer, para um valor específico de N, realizando T simulações.

O programa deve ler dois números inteiros N e T (separados por <espaço>), onde N é a quantidade de amigos, T é a quantidade de simulações. A saída deve ir até 5 casas decimais. Utilize uma seed de zero (0) para garantir reprodutibilidade.

NOTE que o input deve ser: N<espaço>T

Exemplo de input e output

input = 2 100000

output = 0.50030

"""

import random


def fenoSupreendente(N, T):
    random.seed(0)
    contador = 0
    for _ in range(T):

        perm = random.sample(range(N), N)

        atual = 0
        JáCirculados = [False] * N
        tamanho = 0
        terminou = False

        while not JáCirculados[atual]:
            JáCirculados[atual] = True
            atual = perm[atual]
            tamanho += 1

            if atual == 0:
                terminou = True
                break

        if terminou and tamanho == N:
            contador += 1

    p = contador / T
    print(f"{p:.5f}")


entrada = input().strip()
N, T = map(int, entrada.split())
fenoSupreendente(N, T)
