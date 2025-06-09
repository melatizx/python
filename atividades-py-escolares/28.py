n1 = float(input("Informe 1° numero: "))
n2 = float(input("Informe 2° numero: "))
n3 = float(input("Informe 3° numero: "))
if(n1>n2 and n1>n3):
  print("Maior: ", n1)
elif(n2>n1 and n2>n3):
  print("Maior: ", n2)
else:
  print("Maior: ", n3)