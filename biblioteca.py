"""imprimir nomes"""


def imprime_nome(nome):
    print(f"Olá, {nome}")


"""imprimir 1,22,333,4444,55555"""


def numero(n1):  # rep 1,22,333,4444#
    for x in range(0, n1 + 1):
        for i in range(x):
            print(x, end=" ")
        print()


"""contar quantas vogais"""


def vogais(texto):
    cont = 0
    for x in texto:
        if x in "aeiou":
            cont += 1
    print(cont)


"""receber dois numeros e multiplicar e retornar"""


def estoque(nome, quantidade, valorUni):
    valorTotal = quantidade * valorUni
    return nome, valorTotal


"""receber um numero e dizer se é negativo, positivo ou 0"""


def numer(numb):
    if numb > 0:
        return 'P'
    elif numb == 0:
        return "Z"
    else:
        return 'N'


""" receber dois numeros, somar e printar"""


def soma(n1, n2):
    print(n1 + n2)


"""  receber numeros indefinidos e somar( jogar na tupla)"""


def somaT(*a):
    soma = sum(a)
    print(soma)


""" receba um texto e mostre a quantidade de letras e imprimir o texto ao contrario"""


def textoReverso(texto):
    cont = 0
    for x in range(len(texto - 1), -1, -1, -1):
        if texto[x] != " ":
            cont += 1
        print(texto[x], end="")
    print(cont)

""" receber uma lista de numeros e não vai repetir os numeros iguais"""
def listaNumeros(lista):
    novaLista=[]
    for x in lista:
        if x not in novaLista:
            novaLista.append(x)
    print(novaLista)
""" receber uma lista de numeros e não vai repetir os numeros iguais com python(set)"""
def lista2(lista):
    novalista=[]
    novalista=set(lista)
    print(novalista)