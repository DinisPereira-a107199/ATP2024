print("Bora jogar 'Adivinha o número'! Existem duas modalidades: 1 - O computador pensa num número e o jogador tenta acertar ou 2 - O jogador pensa num número e o computador terá de acertar.\nAs regras sao simples:\n-Após cada tentativa o computador ou o jogador tera que responder com 'Acertou', 'O número que pensei é maior' ou 'O número que pensei é menor', até chegar ao número misterioso;\n-O jogador e o computador so puderao escolher um número entre 0 e 100.")
mod = input("Introduza a modalidade pretendida:")
i = 50
max = 100
min = 0
tent = 0
tent2 = 1

while mod != "1" and mod != "2":
    print("Porfavor introduza dados validos.")
    mod = input("Introduza a modalidade pretendida:")

if mod == "1":
    import random
    num = random.randint(0,100)
    print("Tente adivinhar o numero em que estou a pensar!")
    resp = int(input("Qual a sua resposta?"))
    if resp == num:
        print("Acertou em 1 tentativa, Parabéns!")
    while resp > 100 or resp < 0:
        print("Porfavor introduza dados válidos:")
        resp = int(input("Qual a sua resposta?"))
    while resp != num:
        tent = tent + 1
        if resp > num:
            print("O número que pensei é Menor. Tente novamente.")
            resp = int(input("O número que pensei é Menor"))
            while resp > 100 or resp < 0:
                print("Porfavor introduza dados válidos:")
                resp = int(input("Qual a sua resposta?"))
        elif resp < num:
            print("O número que pensei é Maior. Tente novamente.")
            resp = int(input("O número que pensei é Maior"))
            while resp > 100 or resp < 0:
                print("Porfavor introduza dados válidos:")
                resp = int(input("Qual a sua resposta?"))
    print(f"Acertou, Parabéns! Contudo demorou {tent} tentativas!")

elif mod == "2":
    print("Está a pensar no numero 50?")
    resp2 = input("Qual a sua resposta?")
    if resp2 == "Certo":
        print("Eu sabia, consegui acertar com 1 tentativa!")
    while resp2 != "Certo":
        if resp2 == "O numero que pensei é maior":
            tent2 = tent2 + 1
            min = i
            i = (max + i)//2
            if i == 99:
                i = i + 1
            print(f"Está a pensar no numero {i}?")
            resp2 = input("Qual a sua resposta?")
        elif resp2 == "O numero que pensei é menor":
            tent2 = tent2 + 1
            max = i
            i = (min + i)//2
            print(f"Está a pensar no numero {i}?")
            resp2 = input("Qual a sua resposta?")
        else:
            print("Porfavor introduza dados válidos:")
            resp2 = input("Qual a sua resposta?")
    print(f"Eu sabia! Pena que demorei {tent2} tentativas...")
