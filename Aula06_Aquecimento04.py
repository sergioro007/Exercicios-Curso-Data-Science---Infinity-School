print("**********************************")
print("*      SISTEMA DE NOTAS          *")
print("**********************************")
print("")

somanotas = 0
medianotas = 0
quantnotas = 0
digitar = "S"

while digitar == "S" or digitar == "s":
    nota = float(input("Digite a nota: "))
    quantnotas += 1
    somanotas = somanotas + nota
    print ("")
    digitar = str(input("Deseja digitar nova nota? (S/N) "))
    print ("")

print (f'O Aluno somou {somanotas} pontos em {quantnotas} provas.')
print ("")
print (f'Sua média é: ', (somanotas/quantnotas))

