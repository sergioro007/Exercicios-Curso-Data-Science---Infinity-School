# Utilizando FOR, imprima seu primeiro nome com:
# 1) As letras uma abaixo da outra;
# 2) As letras uma ao lado da outra

nome = str(input("Digite uma palavra: "))
i = 0

for i in nome:
    print(i, sep = " ")

print ("")

for i in nome:
    print(i, end = " ")

print("")



