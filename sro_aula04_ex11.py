# Aula 04 - Exercício: 11 - Orçamento para clientes/Loja de tintas

import math

print("*********************************************************")
print("*                    TINTAS BRASIL                      *")
print("*                                                       *")
print("*               FAÇA SEU ORÇAMENTO AQUI                 *")
print("*********************************************************")
print("")


area=float(input("Digite a medida da área a pintar (em metros quadrados): "))
print("")

volumeNecessario=area/3
preco=80.00

qtdeLatas=(volumeNecessario/18)
qtdeArred=math.ceil(qtdeLatas)

orcamento=qtdeArred * preco

print(f"Você precisará de {volumeNecessario:,.2f} litros.")
print("")
print(f'Para suprir essa quantidade, adquira {qtdeArred:,.2f} latas de 18 litros.')
print("")
print(f'*** ORÇAMENTO ***')
print("")
print(f'{qtdeArred:,.2f} x R$ {preco} = R$ {orcamento:,.2f}')
print("")

if orcamento <= 300:
    print("Forma de pagamento: à vista ou cartão de crédito em 1x")
elif orcamento <= 600:
    print("Forma de pagamento: à vista ou cartão de crédito em 2x")
elif orcamento <= 1000:
    print("Forma de pagamento: à vista ou cartão de crédito em 3x")
else:
    print("Forma de pagamento: à vista ou cartão de crédito em 4x")

print("")
print("Obrigado pela preferência!")
