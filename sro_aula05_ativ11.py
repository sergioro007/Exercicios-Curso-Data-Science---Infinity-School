print ("*******************************************")
print("*    TENTE ACERTAR O VALOR SECRETO         *")
print ("*******************************************")
print("")

palpite = float(input("Digite um número entre 0 e 10: "))
print ("")
numSecreto = 8

while True:
    if palpite != numSecreto:
        print ("Você não acertou.")
        print("")
        if palpite < numSecreto:
            print ("Seu palpite foi MENOR que o número secreto!")
            palpite = float(input("Digite um número entre 0 e 10: "))
            print("")
        else:
            print("Seu palpite foi MAIOR que o número secreto!")
            palpite = float(input("Digite um número entre 0 e 10: "))
            print("")
        continue
    else:
        print ('Você ACERTOU! ')
        print (f'Seu palpite foi {palpite} e o número secreto é {numSecreto}')
        print("")
        break
