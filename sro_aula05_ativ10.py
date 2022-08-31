
print ("*******************************************")
print("*      SISTEMA - CONFERÊNCIA DE NOTAS      *")
print ("*******************************************")
print("")

nota = float(input("Digite uma nota entre 0 e 10: "))
print ("")

while True:
    if nota < 0 or nota > 10:
        print ("VALOR INVÁLIDO")
        nota = float(input("Digite uma nota entre 0 e 10: "))
        print("")
        continue
    else:
        print (f'A nota digitada foi: {nota}')
        print("")
        break
