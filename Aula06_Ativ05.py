# Solicite ao usuário um limite inferior e um superior,
# depois informe quantos números pares existem no intervalo.

contaPares = 0

while True:
    numeroMenor = int(input("Digite o menor número do intervalo a analisar: "))
    numeroMaior = int(input("Digite o maior número do intervalo a analisar: "))
    if numeroMenor < numeroMaior:
        break
    else:
        print("Você digitou os limites do intervalo de forma invertida!")
        print("Digite novamente.")
        print("")

for i in range (numeroMenor, numeroMaior+1):
    if i % 2 == 0:
        contaPares = contaPares + 1
    else:
        contaPares = contaPares

print("")
print (f'No intervalo de {numeroMenor} até {numeroMaior} temos {contaPares} números pares')




