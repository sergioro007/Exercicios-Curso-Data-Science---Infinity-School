
print("*************************************")
print("*             CALCULADORA           *")
print("*************************************")
print("")



calcular="S"

while calcular == "S" or calcular == "s":
    numUm = int(input("Digite o primeiro número: "))
    print("")
    numDois = int(input("Digite o segundo número: "))
    print("")
    operacao=str(input("Qual operação você deseja realizar (+, -, x ou /): "))
    if operacao == "+":
        soma=numUm+numDois
        print(f'{numUm} + {numDois} = {soma}')
        print("")
    elif operacao == "-":
        dif = numUm - numDois
        print(f'{numUm} - {numDois} = {dif}')
        print("")
    elif operacao == "x":
        mult = numUm * numDois
        print(f'{numUm} x {numDois} = {mult}')
        print("")
    elif operacao =="/":
        div = numUm / numDois
        print(f'{numUm} : {numDois} = {div}')
        print("")
    else:
        print("VOCÊ DIGITOU UM OPERADOR DESCONHECIDO")
    calcular=str(input("Deseja efetuar novo cálculo (S/N)? "))
