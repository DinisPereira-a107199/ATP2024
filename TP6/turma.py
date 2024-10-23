def menu():
    print(""" 
    ------------Menu------------
    (1) Criar Turma
    (2) Inserir Aluno
    (3) Listar a Turma
    (4) Consultar Aluno por ID
    (5) Guardar a turma num ficheiro
    (6) Carregar uma turma dum ficheiro
    (0) Sair
    ----------------------------""")


def inserirAluno(lista, id, nome, notas): #testar
    if not existeAluno(lista, id):
        notaTPC = int(input("Qual a nota do TPC?"))
        notas.append(notaTPC)
        notaProj = int(input("Qual a nota do projeto?"))
        notas.append(notaProj)
        notaTeste = int(input("Qual a nota do teste?"))
        notas.append(notaTeste)
        aluno = (nome, id, notas)
        lista.append(aluno)
    else:
        print(f"O aluno com o ID {id} ja existe.")
    return lista

def listarTurma(turma, nomet):
    print(f"--------------------{nomet}-------------------")
    for a in turma:
        nome, ident, notas = a
        print(f" Aluno: {nome} | ID: {ident} | Notas: {notas}")
    print("-----------------------------------------------")
    return

def existeAluno(turma, id):
    cond = False
    for a in turma:
        if a[1] == id:
            cond = True
    return cond

def consultaAluno(turma, id):
    if existeAluno(turma, id):
        for a in turma:
            nome, ident, notas = a
            if id == ident:
                print(f" Aluno: {nome} | ID: {ident} | Notas: {notas}")
    else:
        print("Não existe um aluno com esse id.")
    return

def guardarFicheiro(turma, nomef):
    file = open(f"./Aula6/{nomef}.txt","w")
    for a in turma:
        file.write(a[0] + "::" + a[1] + "::" + str(a[2][0]) + "::" + str(a[2][1]) + "::" + str(a[2][2]) + "\n")
    file.close()

def buscarficheiro(turma, nomef):
    file = open(f"./Aula6/{nomef}.txt")
    for linha in file:
        campos = linha.split("::")
        campos3 = [int(campos[2]), int(campos[3]), int(campos[4])]
        aluno = (campos[0], campos[1], campos3)
        turma.append(aluno)
    file.close()
    return turma


opcao = "1"
while opcao != "0":
    menu()
    opcao = input("Opcao:")
    if opcao == "1":
        nomet = input("Insira o nome da turma:")
        turma1 = []
        print("Turma criada!")
    elif opcao == "2":
        nome = input("Introduza o nome do aluno:")
        iden = input("Introduza o id do aluno:")
        notas = []
        turma = inserirAluno(turma1, iden, nome, notas)
    elif opcao == "3":
        listarTurma(turma1, nomet)
    elif opcao == "4":
        iden2 = input("Qual o id do aluno?")
        consultaAluno(turma1, iden2)
    elif opcao == "5":
        guardarFicheiro(turma1, nomet)
        print("Ficheiro guardado!")
    elif opcao == "6":
        nomef = input("Qual o ficheiro que deseja carregar?")
        nomet = nomef
        turma1.clear()
        buscarficheiro(turma1, nomef)
        print("Ficheiro carregado!")
