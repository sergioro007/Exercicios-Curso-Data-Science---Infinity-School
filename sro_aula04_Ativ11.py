

avalia = "S"

print("****************************************************")
print("*             UNIVERSIDADE VIRTUAL                 *")
print("*         SISTEMA DE CONTROLE DE NOTAS             *")
print("****************************************************")
print("")


while avalia == "S" or avalia == "s":
    aluno = str(input("Digite o Nome do Aluno: "))
    print("")
    disciplina = str(input("Digite o Nome da Disciplina: "))
    print("")
    turno = str(input("Digite o Turno do Aluno: "))
    print("")
    notaUm = float(input("Digite a Nota da 1a. Avaliação: "))
    print("")
    notaDois = float(input("Digite a Nota da 2a. Avaliação: "))
    print("")

    media = (notaUm + notaDois)/2

    print(f'ALUNO(A): {aluno}')
    print(f'DISCIPLINA: {disciplina}')
    print(f'TURNO: {turno}')

    if media >= 7:
        print(f'Aluno APROVADO com CONCEITO "A"')
        print(f'MÉDIA: {media}')
    elif media < 7 and media >= 5:
        print(f'Aluno APROVADO com CONCEITO "B"')
        print(f'MÉDIA: {media}')
    elif media < 5 and media > 4:
        print(f'Aluno precisará fazer PROVA FINAL')
        print(f'MÉDIA: {media}')
    else:
        print(f'Aluno REPROVADO')
        print(f'MÉDIA: {media}')

    print("")
    avalia = str(input("Deseja avaliar outro aluno? (S/N): "))
