# criar uma variável com um nome da pessoa
# verificar quantas vogais e quantas consoantes existem no nome informado


nome = str(input("Digite o seu nome completo: "))

vogais = 0
consoantes = 0

for i in nome:
    if i in 'aeiouAEIOU':
        vogais += 1
    if i in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        consoantes += 1

print ("")
print (f'O nome {nome} tem {vogais} vogais e {consoantes} consoantes')