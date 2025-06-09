i = 0
n = []
for p in range(i, 10):
  n.append(int(input(f"Digite o {i+1}º numero: ")))
  i = i+1
maior = max(n)
print(f"Maior: {maior}")
menor = min(n)
print(f"Menor: {menor}")