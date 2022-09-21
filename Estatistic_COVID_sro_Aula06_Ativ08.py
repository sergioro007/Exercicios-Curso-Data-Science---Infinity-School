# Recebe dados de 10 pacientes sobre o nível de gravidade dos sintomas da COVID-19
# Ao final, informa a quantidade e o percentual de pacientes em cada nível.

print ("")
print ("*******************************************************************")
print ("*               SISTEMA DE ESTATÍSTICA DE PACIENTES               *")
print ("*                            COVID-19                             *")
print ("*******************************************************************")
print ("")

sintomasLeves = 0
sintomasMedios = 0
sintomasGraves = 0
i = 0



while i < 10:
    print("Por favor, indique em que nível estão seus sintomas:")
    resposta = int(input("\n[1] Sintomas Leves \n[2] Sintomas Moderados \n[3] Sintomas Graves \n "))
    if resposta == 1:
        sintomasLeves += 1
        i += 1
    elif resposta == 2:
        sintomasMedios += 1
        i += 1
    elif resposta == 3:
        sintomasGraves += 1
        i += 1
    else:
        print ("Você digitou uma opção inválida!")
        print ("")



totalPacientes = sintomasLeves + sintomasMedios + sintomasGraves
percentLeves = (sintomasLeves / totalPacientes)*100
percentMedios = (sintomasMedios / totalPacientes)*100
percentGraves = (sintomasGraves / totalPacientes)*100

print ("")
print (f'* ESTATÍSTICAS DA AMOSTRA DE {i} PACIENTES - COVID-19: ')
print ("")
print (f'Pacientes com Sintomas Leves: {sintomasLeves} = {percentLeves} %')
print ("")
print (f'Pacientes com Sintomas Moderados: {sintomasMedios} = {percentMedios} %')
print ("")
print (f'Pacientes com Sintomas Graves: {sintomasGraves} = {percentGraves} %')


