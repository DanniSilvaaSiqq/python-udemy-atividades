nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if not nome or not idade:
    print("Desculpe, voce deixou campos vazios!")
else:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")

    if "" in nome:
        print("Seu nome contém espacos")
    else:
        print("Seu nome Nao tem espacos")
        
    print(f"Seu nome tem {len(nome)}")
    print(f"A primeira letra do seu nome é {nome[0:1]}")
    print(f"A última letra do seu nome é {nome[4:5]}")
