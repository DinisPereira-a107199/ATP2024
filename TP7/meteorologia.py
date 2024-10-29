tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

def medias(tabMeteo):
    res = []
    for dia in tabMeteo:
        data, tempmin, tempmax, precip = dia
        media = (tempmax + tempmin)/2
        res.append((data,media))
    return res

def guardaTabMeteo(t, fnome):
    f = open(f"{fnome}.txt", "w")
    for dia in t:
        data, tempmin, tempmax, precip = dia
        f.write(f"{data[0]}-{data[1]}-{data[2]} | {tempmin} | {tempmax} | {precip}\n")
    f.close()

def carregaTabMeteo(fnome):
    res = []
    file = open(f"{fnome}.txt", "r")
    for linha in file:
        linha = linha.strip()
        campos = linha.split("|")
        data = campos[0].split("-")
        tuplo = ((int(data[0]),int(data[1]),int(data[2])), float(campos[1]), float(campos[2]), float(campos[3])) #posso dar unpack aos tuplos para nao usar indices
        res.append(tuplo)
    file.close()
    return res

def minMin(tabMeteo):
    minima = tabMeteo[0][1]
    for _, min, *_ in tabMeteo: 
        if minima > min:
            minima = min
    return minima

def amplTerm(tabMeteo):
    res = []
    for dia in tabMeteo:
        data, tempmin, tempmax, precip = dia
        amplt = tempmax - tempmin
        res.append((data,amplt))
    return res

def maxChuva(tabMeteo):
    max_prec = tabMeteo[0][3]
    for data,_,_, prec in tabMeteo:
        if prec > max_prec:
            max_prec = prec
            max_data = data
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    res = []
    for dia in tabMeteo:
        data, tempmin, tempmax, precip = dia
        if precip > p:
            res.append((data,precip))
    return res


def maxPeriodoCalor(tabMeteo, p):
    i = 0
    maior = 0
    for dia in tabMeteo:
        data, tempmin, tempmax, precip = dia
        if precip < p:
            i = i + 1
        else:
            if i > maior:
                maior = i
            i = 0
        if i > maior:
            maior = i
    return maior

import matplotlib.pyplot as plt

def grafTabMeteoT(t):
    data = [f"{ano} - {mes} - {dia}" for (ano, mes, dia), *_ in t]
    temps_min = [dia[1] for dia in t]
    temps_max = [dia[2] for dia in t]
    plt.plot(data, temps_min, label = "Temperatura Min", color = "black", marker = "*")
    plt.plot(data, temps_max, label = "Temperatura Max", color = "red", marker = ".")
    plt.legend()
    plt.xlabel("Dia")
    plt.ylabel("Temperatura, ºC")
    plt.title("Temperatura Max e Min")
    plt.show()
    return

def grafTabMeteoP(t):
    data = [f"{ano} - {mes} - {dia}" for (ano, mes, dia), *_ in t]
    pluv = [dia[3] for dia in t]
    plt.bar(data, pluv, color = "orange")
    plt.xlabel("Dia")
    plt.ylabel("Pluviosidade, mm")
    plt.title("Pluviosidade")
    plt.show()
    return

def menu():
    print(""" 
    ------------Menu------------
    (1) Media
    (2) Guardar Ficheiro
    (3) Carregar Ficheiro
    (4) Temperatura Mín
    (5) Amplitude Térmica
    (6) Máx Pluviosidade
    (7) Dias Chuvosos
    (8) Periodo de Calor Máx
    (9) Gráfico Temperatura
    (A) Gráfico Pluviosidade
    (0) Sair
    ----------------------------""")

opcao = "1"
while opcao != "0":
    menu()
    opcao = input("Opção: ")
    if opcao == "1":
        print(f"A média em cada dia é: {medias(tabMeteo1)}")
    elif opcao == "2":
        fnome = input("Qual o nome do ficheiro?")
        guardaTabMeteo(tabMeteo1, fnome)
        print("Ficheiro Guardado!")
    elif opcao == "3":
        fnome = input("Qual o ficheiro que deseja carregar?")
        tabMeteo1 = carregaTabMeteo(fnome)
        print("Ficheiro Carregado!")
    elif opcao == "4":
        print(f"A temperatura mínima é {minMin(tabMeteo1)}")
    elif opcao == "5":
        print(f"A amplitude térmica em cada dia foi: {amplTerm(tabMeteo1)}")
    elif opcao == "6":
        print(f"A máxima pluviosidade for em : {maxChuva(tabMeteo1)}")
    elif opcao == "7":
        p = float(input("Qual o limite mínimo de pluviosidade?"))
        print(f"Os dias chuvosos foram: {diasChuvosos(tabMeteo1, p)}")
    elif opcao == "8":
        p = float(input("Qual o limite máximo de pluviosidade?"))
        print(f" O maior período de calor foi: {maxPeriodoCalor(tabMeteo1,p)}")
    elif opcao == "9":
        grafTabMeteoT(tabMeteo1)
    elif opcao == "A" or opcao == "a":
        grafTabMeteoP(tabMeteo1)
print("Volte Sempre!")
    