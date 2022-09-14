print("**********************************")
print("*      SISTEMA DE NOTAS          *")
print("**********************************")
print("")

somanotas = 0
medianotas = 0
quantnotas = 1

while True:
    nota = float(input(f'Digite a {quantnotas}a. nota: '))
    somanotas = somanotas + nota
    print ("")
    digitar = int(input("Deseja digitar nova nota?\n [1] Sim\n [2] Não\n "))
    print ("")
    if digitar == 2:
        break
    else:
        quantnotas += 1


print (f'O Aluno somou {somanotas} pontos em {quantnotas} provas.')
print ("")
print (f'Sua média é: ', (somanotas/quantnotas))

