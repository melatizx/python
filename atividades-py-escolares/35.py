import math
area = float(input("Informe a area total: "))
tinta = 18
valor = 80
qtd_latas = math.ceil(area/tinta)
valort = qtd_latas*valor
print(f"Quantidade de latas necessarias: {qtd_latas}")
print(f"Valor: {valort}")