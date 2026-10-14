# Operadores lógicos
# and (e) or (ou) not (nao)
# and - todas as condicoes precisam ser verdadeiras.
# Se qualquer valor for considerado falso,
# a expressao inteira será avaliada naquele valor
# Sao considerados falsy 
# 0 0.0 '' False
# também existe o tipo None que é 
# usado para representar um nao valor

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"

if entrada == "E" or entrada == "e" and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")

# Avaliacao de curto circuito
#print(True and False and True)

# Todas precisam ser True