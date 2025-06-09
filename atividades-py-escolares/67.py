i = 0
n = 0
v = []
e = []
d = []
gp = []
gc = []
pontos = []
saldo = []
tab = []
for l in range(i, 4):
  desempenho = tuple()
  time = print("Time: ")
  for p in range(n, 4):
    v = int(input("Vitorias: "))
    e = int(input("Empates: "))
    d = int(input("Derrotas: "))
    gp = int(input("Gols Pro: "))
    gc = int(input("Gols Contra: "))
    pv = v * 3
    pe = e
    pontos = pv + pe
    saldo = gp - gc
    n = n+1
  desempenho = pontos, v, e, d, gp, gc, saldo
  tab.append(desempenho)
  i = i+1