# solicita ao usuário que digite cinco nomes, em seguida, imprime  a lista

print ("Digite o nome dos cinco participantes: ")

contador = 0
lista = []

for contador in range (0,5):
    nome = str(input(f'Participante {contador+1} : ' ))
    lista.append(nome)

print ("")
print ("Escalação da Equipe:")

for i in range (0,5):
    print (f'Jogador {i+1} : ', lista[i])

