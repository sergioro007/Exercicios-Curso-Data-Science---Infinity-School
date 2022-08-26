# Aula 04 - Exerc. 13: Converte velocidade m/s em Km/h


print("--------------------------------------------------------")
print(".             CONVERSOR DE VELOCIDADE                   ")
print("--------------------------------------------------------")
print("")

i="S"

while i=="S" or i=="s":
    print("Vamos converter uma velocidade de m/s em Km/h ?")
    print("")
    veloM=int(input("Digite a velocidade em m/s: "))
    print("")
    veloKm=veloM * (3600/1000)
    print(f'{veloM} m/s equivalem a {veloKm:.2f} Km/h')
    print("")
    print("")
    i=str(input("Deseja efetuar outra conversão? (S/N): "))
    print("")


