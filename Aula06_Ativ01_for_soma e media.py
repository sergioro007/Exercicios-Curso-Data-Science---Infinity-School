# Ativ 03: peça 5 números e informe a soma e a médias dos mesmos

i=0
soma = 0
media = 0

for i in range(0,5):
    num = int(input(f'Digite o {i}o. número: '))
    soma = soma + num

media = soma/(i-1)

print(f'A soma dos números é: ', soma)
print ("")
print(f'A média dos números é: ', media)
print

