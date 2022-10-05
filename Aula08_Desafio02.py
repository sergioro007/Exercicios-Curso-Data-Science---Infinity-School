# Pede ao usuário que digite 10 números inteiros e, ao final,
# imprime o maior e o menor entre os digitados
# Imprimir tb a lista completa

numeros = []

for i in range (10):
    num = int(input(f'Digite o {i+1}o. número: '))
    numeros.append(num)

print ()
print(f'O maior dos números da lista é: {max(numeros)}')
print ()
print(f'O menor dos números da lista é: {min(numeros)}')
print ()
print (f'Os números digitados foram: {numeros}')
