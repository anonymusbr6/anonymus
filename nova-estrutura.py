#Sistema de Senha
senha = "123455"
lista = [1,2,3,4,5]
for tentativa in lista:
    chute =  input("Digite sua senha:")
    if(chute == senha):
        print("Acesso Liberado")
        break
    else:
        print("Acesso Negado")
else:
    print("Você excedeu os de números de tentativas")

