# pedir 5 números, adicionar em uma lista.
# informar a média e a soma dos números. Ao final, imprimit todos eles

listaNumeros = []
contador = 1


while contador <= 5:
    numero = int(input(f"Digite o {contador}o. número: "))
    listaNumeros.append(numero)
    contador = contador + 1

print (f'A soma dos elementos da lista é: {sum(listaNumeros)}')
print ()
print (f'A média dos elementos da lista é: {sum(listaNumeros)/len(listaNumeros)}')
print ()

for i in range (5):
    print(listaNumeros[i])