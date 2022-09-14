print("*********************************")
print("*        MAIOR E MENOR          *")
print("*********************************")
print ("")

i = 1
maior = 0
menor = 0

while i <= 10:
    numero = int(input(f'Digite o {i}o. número: '))
    if i == 1:
        maior = numero
        menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

    i += 1
print("")
print (f'O maior número é: ', maior)
print("")
print (f'O menor número é: ', menor)








