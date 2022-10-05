# Programa solicita ao usuário que digite notas enquanto desejar e,
# ao final, imprime a soma, a média e a lista das notas digitadas

print ("**********************************************")
print ("*      SISTEMA DE CONTROLE DE NOTAS          *")
print ("**********************************************")
print ()

notas = []
alunos = []
digitar = "s"
contador = 0

while digitar == "s" or digitar == "S":
    aluno = str(input("Digite o nome do(a) aluno(a): "))
    alunos.append(aluno)
    nota = float(input("Digite a nota do aluno(a): "))
    notas.append(nota)
    contador = contador + 1
    print ()
    digitar = str(input(f'Deseja incluir nova nota? \n [s] Sim \n [n] Não \n'))


print ()
print ("### RESULTADOS ###")
print ()

print (f'Total de notas digitadas: {contador}')
print ()
for i in range(len(alunos)):
    print (f'ALUNO(A): {alunos[i]} - NOTA: {notas[i]}')

print ()
print (f'A soma das notas dessa turma é: {sum(notas)}')
print ()
print (f'A média da turma é: {sum(notas)/len(notas)}')
print ()