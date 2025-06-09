qtd_animais = {"C": 0, "R": 0, "S": 0}
pctg_animais = {"C":0, "R":0, "S":0}

casos = int(input())

for i in range (casos):
    x = list(input().split(" "))
    if x[1] == "C":
        qtd_animais["C"] = qtd_animais["C"]+int(x[0])
    elif x[1] == "R":
        qtd_animais["R"] = qtd_animais["R"]+int(x[0])
    else:
        qtd_animais["S"] = qtd_animais["S"]+int(x[0])
    x.clear()

total = [qtd_animais["C"], qtd_animais["R"], qtd_animais["S"]]
total = sum(total)

pctg_animais["C"] = qtd_animais["C"]/total*100
pctg_animais["R"] = qtd_animais["R"]/total*100
pctg_animais["S"] = qtd_animais["S"]/total*100

print(f"""Total: {total} cobaias
Total de coelhos: {qtd_animais["C"]}
Total de ratos: {qtd_animais["R"]}
Total de sapos: {qtd_animais["S"]}
Percentual de coelhos: {pctg_animais["C"]:.2f} %
Percentual de ratos: {pctg_animais["R"]:.2f} %
Percentual de sapos: {pctg_animais["S"]:.2f} %""")