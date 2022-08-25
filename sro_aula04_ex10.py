# Aula 04 - Exerc. 10: Solicita 4 notas de um aluno e, ao final, imprime as notas e a média do aluno

i = "S"

print("============================================================")
print("#             SISTEMA DE CONTROLE DE NOTAS                 #")
print("#                    ESCOLA EXEMPLO                        #")
print("============================================================")
print ("")

while i=="S" or i=="s":
    aluno=str(input("Digite o nome do(a) aluno(a): "))
    print("")
    serie=int(input("Digite a série do(a) aluno(a): "))
    print("")
    disciplina = str(input("Digite a disciplina: "))
    print("")
    turno=str(input("Digite o turno do(a) aluno(a) (M-Manhã/T-Tarde/N-Noite): "))
    while turno !="M" and turno !="T" and turno != "N" :
        print("")
        print("Turno Inválido! Digite novamente.")
        print("")
        turno = str(input("Digite o turno do(a) aluno(a) (M-Manhã/T-Tarde/N-Noite): "))

    print("")
    notaUm = float(input("Digite a nota da Avaliação 1: "))
    print("")
    notaDois = float(input("Digite a nota da Avaliação 2: "))
    print("")
    notaTres = float(input("Digite a nota da Avaliação 3: "))
    print("")
    notaQuatro = float(input("Digite a nota da Avaliação 4: "))
    print("")
    somanota = notaUm + notaDois + notaTres + notaQuatro
    media = somanota / 4
    print("******* RESULTADO DO ALUNO ********")
    print("")
    print(f'ALUNO(A): {aluno}')
    print(f'SÉRIE: {serie}')
    print(f'DISCIPLINA: {disciplina}')
    print(f'TURNO: {turno}')
    print("")
    print(f'Avaliação 1: {notaUm}')
    print(f'Avaliação 2: {notaDois}')
    print(f'Avaliação 3: {notaTres}')
    print(f'Avaliação 4: {notaQuatro}')
    print("")
    print(f'A média do aluno é: {media}')
    print("")
    if media < 6.0 :
        print("O aluno está REPROVADO.")
    else :
        print("O aluno está APROVADO.")
    print("")
    i = str(input("Deseja lançar as notas de outro(a) aluno(a)? (S/N): "))

print("Obrigado por utilizar o Sistema Hipotético.")