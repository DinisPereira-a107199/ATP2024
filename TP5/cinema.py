cinema1 = []

def existeSala(cinema, sala):
    cond = False
    for s in cinema:
        if s[-1] == sala[-1]:
            cond = True
    return cond

def inserirSala(cinema, sala):
    if not existeSala(cinema, sala):
        cinema.append(sala)
    else:
        print("Essa sala já existe")
    return cinema


def listarCinema(cinema):
    print("-----Filmes em Exibição-----")
    for sala in cinema:
        nlugares, vendidos, filme, nome = sala
        print(f" -{filme}")
    print("----------------------------")
    return

def emExibicao(cinema, filmex):
    cond = False
    for sala in cinema:
        if sala[2] == filmex:
            cond = True
    return cond


def disponivel(cinema, filmex, lugar):
    cond = False
    for sala in cinema:
        nlugares, vendidos, filme, nome = sala
        if filmex == filme:
            if lugar not in vendidos:
                cond = True
    return cond

def vendebilhete(cinema, filmex, lugar):
    if disponivel(cinema, filmex, lugar):
        for sala in cinema:
            nlugares, vendidos, filme, nome = sala
            if filme == filmex:
                vendidos.append(lugar)
    else:
        print("O lugar não está disponivel")
    return cinema

def listardisponibilidades(cinema):
    print("-------------------------------------Salas disponiveis---------------------------------------")
    for sala in cinema:
        nlugares, vendidos, filme, nome = sala
        disponiveis = nlugares - len(vendidos) 
        if disponiveis != 0:
            print(f"Nome : {nome} | Filme em exibição: {filme} | Nº  de Lugares Disponiveis: {disponiveis}")
        else:
            print(f"Nome: {nome} | Filme em exibição: {filme} | Encontra-se cheia.")
    print("---------------------------------------------------------------------------------------------")
    return

def removerSala(cinema, nomesala):
    for sala in cinema:
        nlugares, vendidos, filme, nome = sala
        if nomesala == nome:
            cinema.remove(sala)
    return cinema


def menu():
    print(""" 
    ------------Menu------------
    (1) Reset
    (2) Inserir Sala
    (3) Listar Cinema
    (4) Listar Salas Disponiveis
    (5) Venda de Bilhetes
    (6) Remover Sala
    (0) Sair
    ----------------------------""")

opcao = "1"
while opcao != "0":
    menu()
    opcao = input("Selecione uma opção:")
    while opcao not in ["1","2","3","4","5","6","0"]:
        print("Introduza uma opção válida:")
        opcao = input("Selecione uma opção:") 
    if opcao == "1":
        cinema1.clear()
        print("A lista de salas foi apagada!")
    elif opcao == "2":
        nome = input("Qual é o nome da sala?")
        nlugares = int(input("Quantos lugares tem a sala?"))
        filme = input("Qual o filme em exibição na sala?")
        vendidos = []
        sala = (nlugares, vendidos, filme, nome)
        inserirSala(cinema1,sala)
        print("A sala foi guardada!")
    elif opcao == "3":
        listarCinema(cinema1)
    elif opcao == "4":
        listardisponibilidades(cinema1)
    elif opcao == "5":
        filme2 = input("Qual o filme que deseja ver?")
        if emExibicao(cinema1,filme2):
            N = int(input("Quantos bilhetes deseja comprar?"))
            for i in range(N):
                lugar = input("Qual o lugar onde se deseja sentar?")
                vendebilhete(cinema1, filme2, lugar)
            print("Lugares comprados!")
        else:
            print("O filme não está em exibição.")
    elif opcao == "6":
        nome2 = input("Qual é o nome da sala que quer remover?")
        removerSala(cinema1,nome2)
        print("A sala foi removida!")
