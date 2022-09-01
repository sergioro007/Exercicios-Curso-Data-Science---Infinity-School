
i = 1
soma = 0
continua = "S"

while True:
    if continua == "S" or continua == "s":
        parcela = int(input(f"Digite a {i}a. parcela:  "))
        print("")
        soma = soma + parcela
        i = i + 1
        continua = str(input("Deseja digitar outra parcela (S/N)?  "))
        print("")
    else:
        break

media = soma / (i - 1)
print("")
print(f'Você digitou {i - 1} parcelas.')
print("")
print (f'A soma das parcelas digitadas é: {soma}')
print("")
print (f'A média das parcelas digitadas é: {media}')
