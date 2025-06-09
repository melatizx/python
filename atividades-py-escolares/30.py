n1 = int(input("Digite o 1° numero: "))
n2 = int(input("Digite o 2° numero: "))
ope = input("Informe a operação: ")
if(ope=='+'):
  print(f"{n1}+{n2}={n1+n2}")
elif(ope=='-'):
  print(f"{n1}-{n2}={n1-n2}")
elif(ope=='x' or ope=='.' or ope=='X' or ope=='*'):
  print(f"{n1}x{n2}={n1*n2}")
elif(ope==':' or ope=='/' or ope=='÷'):
  print(f"{n1}÷{n2}={n1/n2}")
else:
  print("Operação invalida")