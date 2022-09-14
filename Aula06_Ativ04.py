# pede 10 números inteiros e positivos
# ao final, informar a soma dos pares e a soma dos ímpares

somapares = 0
somaimpares = 0

for i in range(1,11):
    numero = int(input(f'Digite o {i}o. número: '))
    if numero%2 == 0:
        somapares = somapares + numero
    else:
        somaimpares = somaimpares + numero

print ("")
print (f'A soma dos números pares é: {somapares}')
print ("")
print(f'A soma dos números ímpares é: {somaimpares}')
print ("")