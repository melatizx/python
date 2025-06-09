i = 0
soma = 0
for c in range(i,4):
  nota = int(input(f"Digite a {i+1}° nota: "))
  soma = soma+nota
media = soma/4
print(f"Media: {media}")