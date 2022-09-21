# solicita a digitação de um número inteiro e positivo
# calcula o fatorial do núemro fornecido

n = int(input("Digite um número inteiro para descobrir seu fatorial: "))

num = n
m = n * (n - 1)
n = n - 2


while n >= 1:
         y = m * n
         m = y
         n = n - 1

print ("")
print (f'O fatorial de {num} é: {m}')
print ("")
