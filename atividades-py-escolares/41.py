n1 = float(input("Informe 1° numero: "))
n2 = float(input("Informe 2° numero: "))
n3 = float(input("Informe 3° numero: "))
n4 = float(input("Informe 4° numero: "))
n5 = float(input("Informe 5° numero: "))
if(n1>n2 and n1>n3 and n1>n4 and n1>n5):
  print("Maior: ", n1)
elif(n2>n1 and n2>n3 and n2>n4 and n2>n5):
  print("Maior: ", n2)
elif(n3>n1 and n3>n2 and n3>n4 and n3>n5):
  print("Maior: ", n3)
elif(n4>n1 and n4>n2 and n4>n3 and n4>n5):
  print("Maior: ", n4)
else:
  print("Maior: ", n5)