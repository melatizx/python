i = 0
soma = 0
numeros = []
positivos = 0
for i in range(0, 6):
    num = float(input(""))
    if num >= 0:
        numeros.append(num)
        positivos = positivos+1

media = (sum(numeros))/positivos
media2 = "{:.1f}".format(media)

print(f"{positivos} valores positivos")
print(media2)