

print("******************************************")
print("*           SISTEMA DE TESTE)            *")
print("******************************************")
print("")

acesso = "S"
tentativa = 1

while acesso == "S" or acesso =="s":
    if tentativa <= 3:
        usuario=str(input("Digite o seu login: "))
        print("")
        senha=str(input("Digite sua senha: "))
        print("")
        if usuario == "admin" and senha == "619":
            print("ACESSO LIBERADO")
            acesso = "N"
            break
        elif usuario != "admin" or senha != "619":
            print("USUÁRIO OU SENHA INVÁLIDO")
            print("")
            acesso = str(input("Deseja tentar novamente (S/N)? "))
            print("")
            tentativa += 1
    else:
        print("Você excedeu o número permitido de tentativas.")
        print("Fale com o administrador do sistema.")
        break




