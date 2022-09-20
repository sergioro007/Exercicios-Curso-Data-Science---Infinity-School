# Solicita ao usuário um número e mostra a tabuada referente ao mesmo

print ("#######################################################")
print ("#       BEM-VINDO(A) À TABUADA DE MULTIPLICAR         #")
print ("#######################################################")
print ("")

i = 0
j = 1

tabuada = int(input("Você deseja a tabuada de qual número? "))
print ("")

for i in range (i, 10):
    resultado = j * tabuada
    print (f'{j} x {tabuada} = {resultado}', sep = " ")
    j = j + 1