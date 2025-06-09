valor = float(input("Informe o valor do deposito: "))
taxa = float(input("Informe a taxa: "))
rend = (valor*taxa)/100
valor_final = valor+rend
print("Valor após rendimento: ", valor_final, "\n")
print("Rendimento: ", rend, "\n")