# Aula 04 - Exerc. 09 : Solicitar dois número e depois imprimir a soma dos mesmos

print ("**************************************************")
print ("*        CÁLCULO: ADIÇÃO DE DUAS PARCELAS        *")
print ("**************************************************")
print ("")

i = "S"

while i == "S" or i == "s" :
    parcUm = float(input("Digite o primeiro número: "))
    print("")
    parcDois = float(input("Digite o segundo número: "))
    print("")
    soma = parcUm + parcDois
    print (f'A soma de {parcUm} mais {parcDois} é igual a {soma}')
    print("")
    i = str(input("Deseja efetuar outra soma? (S/N) "))

print("")
print ("*** Até a nossa próxima operação! ***")

