"""
Interpolacao básica de strings
s - string
d e i - int
f - float 
.<número de dígitos>f
x e X - Hexadecimal (ABCDEF0123456789)
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou - 
ex.: 0>-100,1.f
Conversion flags - !r !s !a

"""

"""

nome = "Danni"
preco = 1000.95897643
variavel = "%s, o preco é R$%.2f" % (nome, preco)
print(variavel)
print("O hexadecimal de %d é %04x" %(15, 15))

"""

variavel = "ABC"
print(f"{variavel}")
print(f"{variavel: >10}") #Cria um padding para a esquerda >
print(f"{variavel: <10}") #Cria um padding para a direita <
