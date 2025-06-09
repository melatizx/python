i = 0
nome = []
qtd = int(input("Quantos alunos tem na sala do 2ºDS?: "))
for c in (i, qtd):
  nome.append(input(f"Digite o nome do {i+1}º aluno: "))
  i = i+1
print(nome)