import random

print ("*******************************************")
print("*    TENTE ACERTAR O VALOR SECRETO         *")
print ("*******************************************")
print("")

palpite = float(input("Digite um número entre 0 e 10: "))
print ("")
numSecreto = random.randint(0,10)

while True:
    if palpite != numSecreto:
        print ("Você não acertou.")
        print("")
        if palpite < numSecreto:
            print (f'Seu palpite foi MENOR que o número secreto!')
            palpite = float(input("Digite um número entre 0 e 10: "))
            print("")
            continue
        else:
            print(f'Seu palpite foi MAIOR que o número secreto!')
            palpite = float(input("Digite um número entre 0 e 10: "))
            print("")
            continue
    else:
        print ('Você ACERTOU! ')
        print (f'Seu palpite foi {palpite} e o número secreto é {numSecreto}')
        print("")
        break
