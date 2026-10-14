# Avaliacao de curto circuito
# senha = input("Senha: ") or "Sem Senha"
# print(senha)


# Operador lógico "not"
# Usado para inverter expressoes
# not True = False
# not False = True

senha = input("Senha: ")

# if senha == "123456":
    # print("Entrou")
# else:
    # print("Senha incorreta.")

if not senha:
    print("Voce nao digitou nada")

print(not True) #False
print(not False) #True