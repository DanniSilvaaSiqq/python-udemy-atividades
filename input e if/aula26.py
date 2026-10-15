"""
Introducao ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

"""

numero_str = input("Vou dobrar o número que digitar! ")

try:
    print("STR:", numero_str) #aqui printamos que o numero ainda é STR
    numero_float = float(numero_str) #Aqui transformamos o numero de STR em FLOAT
    print("FLOAT", numero_float) #aqui printamos que o numero é FLOAT
    print(f"O dobro de {numero_str} é {numero_float * 2:.2f}") #Aqui dobramos o numero que o usuario coloca
except: #Esse bloco é caso o usuario nao coloque numero 
    print("Isso nao é um número!") #mensagem de erro por falta de numeros validos


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")
# else:
#     print("Isso nao é um número!")