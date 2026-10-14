# Operadores in e not in
# Strings sao iteráveis
# 0 1 2 3 4 5
# D a n n i
# -6-5-4-3-2-1

nome = "Danni"
print(nome[2])
print(nome[-3])
print("n" in nome)
print("c" in nome)
print(10 * "-")
print("dan" not in nome)
print("su" not in nome)
print(10 * "-")

nome = input("Digite seu nome! ")
encontrar = input("Digite o que deseja encontrar! ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} nao está em {nome}")