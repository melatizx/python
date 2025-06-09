sal = float(input("Informe o seu salário atual: "))
perc = float(input("Informe o percentual de aumento: "))
aumento = (sal*perc)/100
novo_sal = sal + aumento
print("O seu salário atual é ", novo_sal, "com aumento de ", aumento)