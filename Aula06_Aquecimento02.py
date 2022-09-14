print("*********************************")
print("*         QUADRADO/CUBO         *")
print("*********************************")
print("")

numero = int(input("Digite um número inteiro: "))
print ("")

classenum = numero%2

quadrado = numero**2
cubo = numero**3

if classenum == 0:
    print (f'O quadrado do numero {numero} é: ', quadrado)
else:
    print (f'O cubo do número {numero} é: ', cubo)
