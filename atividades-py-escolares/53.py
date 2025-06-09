cand1 = 0
cand2 = 0
cand3 = 0
voto = 0
votoB = 0
votof = 0
i = 0
eleit = int(input("Quantos eleitores votaram: "))
for i in range(i, eleit):
  voto = int(input("Em quem você votou: "))
  if (voto == 1):
    cand1 = cand1 + 1
  elif (voto == 2):
    cand2 = cand2 + 1
  elif (voto == 3):
    cand3 = cand3 + 1
  elif (voto >= 4):
    print("Esse candidato não existe. Digite outro candidato")
    i = i - 1
  else:
    votoB = votoB + 1

resultado_eleicao = [(cand1, "Candidato 1"), (cand2, "Candidato 2"),
                     (cand3, "Candidato 3")]
print(resultado_eleicao)
maior = max(resultado_eleicao)
print(f"O {maior[1]} teve {maior[0]} votos")
menor = min(resultado_eleicao)
print(f"O {menor[1]} teve {menor[0]} votos")