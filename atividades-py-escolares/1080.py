numeros = []
for n in range(1, 101):
    numero = int(input())
    numeros.append(numero)

maior = max(numeros)
print(maior)
print(numeros.index(maior)+1)