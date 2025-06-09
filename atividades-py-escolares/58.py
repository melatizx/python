porc = 0
prec = 0
tipoc = (input("Tipo de combustivel: ").lower())
l = float(input("Quantidade de litros: "))

if tipoc == 'a':
  if l <= 20:
    porc = l*3
    prec=l*3.90
    desc=(prec*porc)/100
    valor=prec-desc
    print("Valor a ser pago é R$", valor)
  else:
    porc=l*5
    prec=l*3.90
    desc=(prec*porc)/100
    valor=prec-desc
    print("Valor a ser pago é R$", valor)
elif tipoc == 'g':
  if l<=20:
    porc=l*4
    prec=l*5.50
    desc=(prec*porc)/100
    valor=prec-desc
    print("Valor a ser pago é R$", valor)
  else:
    porc=l*6
    prec=l*5.50
    desc=(prec*porc)/100
    valor=prec-desc
    print("Valor a ser pago é R$", valor)
else:
  print("Tipo de combustivel invalido, informe 'g' para gasolina ou 'a' para alcool.")