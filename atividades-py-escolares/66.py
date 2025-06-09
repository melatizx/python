n = 0
soma = 0
boletim = []
nome = []
media = []
for p in range(n, 2):
  desempenho_aluno = tuple()
  nota = []
  i = 0
  nome = (input(f"Digite o nome do {n+1}º aluno: "))
  for s in range(i, 4):
    nota.append(int(input(f"Informe a {i+1}ª nota: ")))
    i = i + 1
  nota.append(sum(nota) / 4)
  desempenho_aluno = nome, nota
  boletim.append(desempenho_aluno)
  n = n + 1
print(' ')
print("+------------------------------------+")
print(' ')
for b in boletim:
  print(f"Aluno {b[0]} com media {b[1][-1]}")
  print(' ')