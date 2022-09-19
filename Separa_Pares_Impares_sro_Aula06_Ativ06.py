# solicita um intervalo de números e, a partir do mesmo,
# imprime a lista dos pares e a lista dos ímpares separadamente

print ("*************************************************")
print ("*        SEPARAÇÃO DE PARES E ÍMPARES           *")
print ("*************************************************")
print ("")


i = int(input("Digite um número inteiro para início do intervalo: "))
j = int(input("Digite um número inteiro para final do intervalo: "))
print("")
limiteInferior = i
limiteSuperior = j

print(f'Os números pares entre {i} e {j}: ')
for i in range (i,j+1):
    if i % 2 == 0:
        print (i, end="  ")
    else:
        continue
print("")

i = limiteInferior
j = limiteSuperior

print ("")
print(f'Os números ímpares entre {i} e {j}: ')
for i in range (i,j+1):
    if i % 2 != 0:
        print (i, end="  ")
    else:
        continue



print ("")
print ("")

