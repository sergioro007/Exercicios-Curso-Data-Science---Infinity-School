# Aula 04 - Atividade 05: "Fotossensor"


i = "S"

while i == "S" or i =="s" :
    velocidade = int(input("Digite a velocidade do veículo (km/h): "))
    print("")
    if velocidade <= 60 :
        print ("Veículo está na velocidade permitida")
    elif velocidade <= 80 :
        print ("Veículo está em alta velocidade")
    elif velocidade < 120 :
        print ("Veículo está muito rápido")
    else :
        print("Veículo está VUADO!!!")

    i = str(input('Deseja verificar a velocidade de outro veículo? (S/N)  '))

