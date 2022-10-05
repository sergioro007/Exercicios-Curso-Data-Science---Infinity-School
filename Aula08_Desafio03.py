# Pede ao usuário que digite 10 números inteiros e, ao final,
# imprime a lista de números em ordem crescente e em ordem decrescente

numeros = []


for i in range (10):
    num = int(input(f'Digite o {i+1}o. número: '))
    numeros.append(num)

print ()
numeros.sort()
print (f'Lista em ordem crescente: {numeros}')
print ()
numeros.reverse()
print (f'Lista em ordem decrescente: {numeros}')
