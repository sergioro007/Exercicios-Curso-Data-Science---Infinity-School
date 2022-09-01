
i = 1
soma = 0

while i <=5:
    parcela = int(input(f"Digite a {i}a. parcela:  "))
    soma = soma + parcela
    i = i + 1

media = soma / (i - 1)
print("")
print (f'A soma das parcelas digitadas é: {soma}')
print("")
print (f'A média das parcelas digitadas é: {media}')

