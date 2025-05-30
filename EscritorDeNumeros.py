"""
Escreva um programa para lê um número inteiro entre -999.999.999 e 999.999.999 e imprime o equivalente em inglês.

Aqui está uma lista exaustiva de palavras que seu programa deve usar: negative, zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, hundred, thousand, million. Não use hundred quando puder usar thousand, por exemplo, use one thousand five hundred em vez de fifteen hundred.

"""

Numeros_Unidadade = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
Numeros_Decimais_acima_de19 = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
Numeros_Decimais_acima_ate19 = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

Numero_entrado = int(input())
negativo = False

if Numero_entrado < 0:
    negativo = True
    Numero_entrado = Numero_entrado * -1
if Numero_entrado == 0:
    print("zero")


def EscritorDeNumeros(Numero_Escrever):
    Resultado = ""
    if 0 < Numero_Escrever < 10:
        Resultado = Numeros_Unidadade[Numero_Escrever]
    elif 10 <= Numero_Escrever < 20:
        Resultado = Numeros_Decimais_acima_ate19[Numero_Escrever - 10]
    elif 20 <= Numero_Escrever < 100:
        dezena, unidade = divmod(Numero_Escrever, 10)
        Resultado = Numeros_Decimais_acima_de19[dezena - 2]
        if unidade != 0:
            Resultado = (
                Numeros_Decimais_acima_de19[dezena - 2]
                + " "
                + Numeros_Unidadade[unidade]
            )
    elif 100 <= Numero_Escrever < 1000:
        centena, resto = divmod(Numero_Escrever, 100)
        Resultado = Numeros_Unidadade[centena] + " hundred"
        if resto != 0:
            Resultado = (
                Numeros_Unidadade[centena] + " hundred " + EscritorDeNumeros(resto)
            )
    return Resultado


if Numero_entrado < 1000:
    if negativo == True:
        print("negative " + EscritorDeNumeros(Numero_entrado))
    else:
        print(EscritorDeNumeros(Numero_entrado))


elif 1000 <= Numero_entrado < 1000000:
    resultadomilhar, resultadoresto = divmod(Numero_entrado, 1000)
    resultado = EscritorDeNumeros(resultadomilhar) + " thousand"
    if resultadoresto != 0:
        resultado = (
            EscritorDeNumeros(resultadomilhar)
            + " thousand "
            + EscritorDeNumeros(resultadoresto)
        )
    if negativo == True:
        print("negative " + resultado)
    else:
        print(resultado)

elif 1000000 <= Numero_entrado < 1000000000:
    resultadomilhao, resultadoresto = divmod(Numero_entrado, 1000000)
    resultado = EscritorDeNumeros(resultadomilhao) + " million"
    if resultadoresto != 0:
        resultadomilhar, resultadorestocentenas_dezenas = divmod(resultadoresto, 1000)
        resultado = (
            EscritorDeNumeros(resultadomilhao)
            + " million "
            + EscritorDeNumeros(resultadomilhar)
            + " thousand"
        )
        if resultadorestocentenas_dezenas != 0:
            resultado = (
                EscritorDeNumeros(resultadomilhao)
                + " million "
                + EscritorDeNumeros(resultadomilhar)
                + " thousand "
                + EscritorDeNumeros(resultadorestocentenas_dezenas)
            )
    if negativo == True:
        print("negative " + resultado)
    else:
        print(resultado)
