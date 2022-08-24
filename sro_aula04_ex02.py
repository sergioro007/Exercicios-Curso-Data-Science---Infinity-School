# Aula 04 - Exercício 02: Cálculo da Área de um Círculo

print ("**********************************************")
print ("*       CÁLCULO DA ÁREA DE UM CÍRCULO        *")
print ("**********************************************")
print ("")

pi = 3.14159265
i = str("S")


while i == "S" :
    raio = float(input("Digite o raio do círculo: "))
    area = (pi * (raio ** 2))
    print (f"A área do círculo de raio {raio} é: {area}")
    print ("")
    i = str(input("Deseja fazer um novo cálculo (S/N)? "))

print ("Obrigado por utilizar nosso sistema!")

