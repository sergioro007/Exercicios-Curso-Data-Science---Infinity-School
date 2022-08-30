

from random import randint

abrirPorta = "S"


print("*********************************************************")
print("*                                                       *")
print("*                   BEM-VINDO(A)!                       *")
print("*                                                       *")
print("*   VAI ARRISCAR A SORTE NA PORTA DOS DESESPERADOS???   *")
print("*                                                       *")
print("*********************************************************")
print("")

while abrirPorta == "S" or abrirPorta =="s":
    computador = randint(1,4)
    porta = int(input("Escolha uma porta, de 1 a 4:"))
    print("")
    if porta == computador:
        print("PARABÉNS!!! VOCÊ GANHOU UMA BICICLETA CALOI.")
    elif porta != computador and porta == 1:
        print(f'Ahhhh... Você abriu a porta {porta} e ganhou uma MELANCIA.')
        print(f'A porta em que está o prêmio máximo é a porta {computador}.')
    elif porta != computador and porta == 2:
        print(f'Ahhhh... Você abriu a porta {porta} e ganhou uma CANETA BIC.')
        print(f'A porta em que está o prêmio máximo é a porta {computador}.')
    elif porta != computador and porta == 3:
        print(f'Ahhhh... Você abriu a porta {porta} e ganhou um GUARDA-CHUVA.')
        print(f'A porta em que está o prêmio máximo é a porta {computador}.')
    elif porta != computador and porta == 4:
        print(f'Ahhhh... Você abriu a porta {porta} e ganhou uma CAIXA DE GIZ DE CERA.')
        print(f'A porta em que está o prêmio máximo é a porta {computador}.')
    else:
        print("Você digitou um número inválido! Tente novamente!")

    print("")
    abrirPorta=str(input("Deseja abrir outra porta? (S/N)..."))
    print("")




