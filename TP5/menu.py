varinterna = []
def menu():
    print("-------------------Menu-------------------")
    print("1 - Criar lista")
    print("2 - Ler lista")
    print("3 - Soma")
    print("4 - Média")
    print("5 - Maior")
    print("6 - Menor")
    print("7 - Ordenada de forma crescente")
    print("8 - Ordenada de forma decrescente")
    print("9 - Procurar um elemento")
    print("0- Sair") 

import random
def CriarLista(N):
    varinterna.clear()
    for num in range(N):
        varinterna.append(random.randint(1,100))
    return varinterna

def LerLista(N):
    varinterna.clear()
    for num in range(N):
        numeros = int(input("Que número deseja adicionar à lista"))
        varinterna.append(numeros)
    return varinterna

def somaLista(lista):
    soma = 0
    for num in lista:
        soma = soma + num
    return soma

def mediaLista(lista):
    soma = somaLista(lista)
    media = 0
    if len(lista) != 0:
        media = soma/len(lista)
    return media

def maiorLista(lista):
    res = lista[0]
    for i in lista:
        if i > res:
            res = i
    return res

def menorLista(lista):
    res = lista[0]
    for i in lista:
        if i < res:
            res = i
    return res

def estaOrdenadaC(lista):
    i = lista[0]
    cond1 = True
    for elem in lista[1:]:
        if i <= elem:
            i = elem
        else:
            cond1 = False
    if cond1:
        res = "A lista é crescente"
    else:
        res = "A lista nao é crescente"
    return res

def estaOrdenadaD(lista):
    i = lista[0]
    cond1 = True
    for elem in lista[1:]:
        if i >= elem:
            i = elem
        else:
            cond1 = False
    if cond1:
        res = "A lista é decrescente"
    else:
        res = "A lista nao é decrescente"
    return res

def procurarElem(lista, elem):
    for i, element in enumerate(lista):
        if element == elem:
            res = i
    if elem not in lista:
        res = -1
    return res


cond = True
while cond:
    menu()
    print(f"Aqui está a sua lista: {varinterna}")
    opcao = input("Introduza uma opção")
    while opcao not in ["1","2","3","4","5","6","7","8","9","0"]:
        print("Introduza dados válidos:")
        opcao = input("Introduza uma opção")
    if opcao == "1":
        num1 = int(input("Insira o tamanho da lista:"))
        print(CriarLista(num1))
    elif opcao == "2":
        num2 = int(input("Insira o tamanho da lista:"))
        print(LerLista(num2))
    elif opcao == "3":
        print(f"O resultado da soma é {somaLista(varinterna)}")
    elif opcao == "4":
        print(f"O resultado da média é {mediaLista(varinterna)}")
    elif opcao == "5":
        print(f"O maior elemento é {maiorLista(varinterna)}")
    elif opcao == "6":
        print(f"O menor elemento é {menorLista(varinterna)}")
    elif opcao == "7":
        print(estaOrdenadaC(varinterna))
    elif opcao == "8":
        print(estaOrdenadaD(varinterna))
    elif opcao == "9":
        elem = int(input("Qual o elemento que deseja saber a posição?"))
        print(f"O elemento {elem} encontra-se na posição {procurarElem(varinterna,elem)}")
    elif opcao == "0":
        cond = False
        print(f"Aqui está a sua lista: {varinterna}")
        print("Volte sempre!")
    else:
        print("Introduza dados válidos:")
        opcao = input("Introduza uma opção")