# Cálculo e avaliação do IMC do paciente



i = "S"

while i == "S" or i =="s" :
    altura = float(input("Digite a altura do paciente: "))
    peso = float(input("Digite o peso do paciente: "))
    imc = peso / altura ** 2
    print("")
    print (f'Peso do Paciente: {peso} kg')
    print ("")
    print(f'Altura do Paciente: {altura} m')
    print ("")
    print(f'IMC do Paciente: {imc}')
    print("")
    if imc <= 18.5 :
        print ("Paciente está abaixo do peso normal")
    elif imc <= 24.9 :
        print ("Paciente está com peso normal")
    elif imc <= 29.9 :
        print ("Paciente está com sobrepeso")
    elif imc <= 34.9 :
        print("Paciente está com obesidade Classe I")
    elif imc <= 39.9 :
        print("Paciente está com obesidade Classe II")
    else :
        print("Paciente está com obesidade Classe III")


    i = str(input('Deseja verificar o IMC de outro paciente? (S/N)  '))

