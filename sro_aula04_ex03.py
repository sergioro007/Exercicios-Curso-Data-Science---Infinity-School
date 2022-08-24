# Aula 04 - Exercício 03: Faça um programa que peça o raio de um círculo, calcule e mostre a
# sua área usando a biblioteca MATH.



print ("***********************************************")
print ("*      CÁLCULO DA ÁREA DE UM CÍRCULO          *")
print ("***********************************************")
print ("")

import math
i = str("S")

while i == "S" or i == "s" :
    raio = float(input("Digite o raio do círculo: "))
    area = math.pi * (raio ** 2)
    print (f'A área do círculo de raio {raio} é: {area}')
    print ("")
    i = str(input ("Deseja efetuar um novo cálculo? (S/N) "))

print ("Obrigado por utilizar nosso sistema. Até a proxima!")
