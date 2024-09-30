print("""Vamos jogar 21 fósforos!
      \nExistem duas modalidades: 1 - O jogador joga em primeiro e o computador em segundo; 2 - O computador começa em primeiro e o jogador em segundo
      \nAqui estão as regras:
      - O jogo começa com 21 fósforos;
      - Cada jogador so pode tirar entre 1 e 4 fósforos de uma vez;
      - Os jogadores jogam à vez;
      - Quem tirar o último fósforo PERDE!""")

print("\nSelecione uma modalidade:")
mod = input("Modalidade (1 ou 2):")

while mod not in ["1","2"]:
    print("Selecione uma modalidade válida!")
    mod = input("Modalidade (1 ou 2):")

max = 21

if mod == "1":
      print("Introduza o número de fósforos que quer retirar")
      while  max > 1:
            nfosf = int(input("Introduza o número de fósforos que quer retirar"))
            while nfosf not  in [1,2,3,4]:
                  print("Introduza o número de fosforos válido:")
                  nfosf = int(input("Introduza o número de fósforos que quer retirar"))
            max = max - nfosf
            print(f"Retirou {nfosf}. Faltam {max} fósforos.")
            pc = 5 - nfosf
            max = max - pc
            print(f"Vou retirar {pc}. Assim ficam a sobrar {max}.")
      nfosf = int(input("Introduza o número de fósforos que quer retirar"))
      while nfosf > max:
            print("É inevitável.")
            nfosf = int(input("Introduza o número de fósforos que quer retirar"))
      print(f"Retirou {nfosf}. Faltam 0 fósforos.")
      print("Ganhei! Sempre que quiseres estou aqui para a desforra.")


if mod == "2":
      while max >= 1:
            if max in [1,6,11,16,21]:
                        if max > 1:
                              import random
                              pc2 = random.randint(1,4)
                              max = max - pc2
                              print(f"Vou retirar {pc2}. Faltam {max} fósforos.")
                              nfosf = int(input("Introduza o número de fósforos que quer retirar"))
                              while nfosf not in [1,2,3,4]:
                                    print("Introduza dados válidos")
                                    nfosf = int(input("Introduza o número de fósforos que quer retirar"))
                              max = max - nfosf
                              print(f"Retirou {nfosf}. Faltam {max} fósforos.")
                        else:
                              max = max - 1
                              print(f"""Vou retirar 1. Faltam {max} fósforos . 
                              Parabéns! Ganhou!!""")
            else:
                  print("Acho que alguém cometeu um erro.. :)")
                  pc2= 0
                  while max >= 1:
                        while max not in [1,6,11,16]:
                              pc2  = pc2 + 1
                              max = max - 1
                        print(f"Vou retirar {pc2}. Faltam {max} fósforos.")
                        nfosf = int(input("Introduza o número de fósforos que quer retirar"))
                        while nfosf not in [1,2,3,4]:
                              print("Introduza dados válidos")
                              nfosf = int(input("Introduza o número de fósforos que quer retirar"))
                        while nfosf > max:
                              print("É inevitável.")
                              nfosf = int(input("Introduza o número de fósforos que quer retirar"))
                        max = max - nfosf
                        print(f"Retirou {nfosf}. Faltam {max} fósforos.")
                        pc2 = 5 - nfosf
                        max = max - pc2   
                  print("Tenta pensar numa estratégia!")
