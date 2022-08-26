# Aula 04 - Exerc. 12: Converte velocidade km/h em m/s


print("--------------------------------------------------------")
print(".             CONVERSOR DE VELOCIDADE                   ")
print("--------------------------------------------------------")
print("")

i="S"

while i=="S" or i=="s":
    print("Vamos converter uma velocidade de Km/h em m/s ?")
    print("")
    veloKm=int(input("Digite a velocidade em Km/h: "))
    print("")
    veloM=veloKm * (1000/3600)
    print(f'{veloKm} Km/h equivalem a {veloM:.2f} m/s')
    print("")
    print("")
    i=str(input("Deseja efetuar outra conversão? (S/N): "))
    print("")


