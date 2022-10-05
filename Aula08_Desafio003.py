# solicita a digitação de 10 números inteiros e positivos
# imprime a soma dos números pares e a soma dos ímpares separadamente
# imprime a lista dos números pares e a dos ímpares, também separadamente

listaPar = []
listaImpar = []
i = 0

while i < 10:
    numero = int(input(f'Digite o {i+1}o. número: '))
    if numero <= 0:
        print ("Você digitou um número inválido (negativo ou zero). Digite novamente.")
    else:
        if numero % 2 == 0:
            listaPar.append(numero)
            i = i + 1
        else:
            listaImpar.append(numero)
            i = i + 1

print ()
listaPar.sort()
listaImpar.sort()

if len(listaPar) > 0:
    print (f'Os número pares digitados foram: {listaPar}, que somam {sum(listaPar)}')
    print ()
else:
    print ("Você não digitou números pares!")
    print ()

if len(listaImpar) > 0:
    print (f'Os números ímpares digitados foram: {listaImpar}, que somam {sum(listaImpar)}')
    print ()
else:
    print("Você não digitou números ímpares!")
    print ()

