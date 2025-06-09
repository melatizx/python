base = float(input("Informe a base: "))
expo = float(input("Informe o expoente: "))
if(base<=0 or expo<=0):
  print("A base/expoente tem que ser maior que zero.")
else:
  num = base**expo
  print(num)