import math
a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))
if(a==0 or b==0 or c==0):
  print("A equação esta incompleta")
else:
  delta = (b*b)-(4*a*c)
  x1 = (-b + math.sqrt(delta))/2*a
  x2 = (-b - math.sqrt(delta))/2*a
print("Raizes: ", x1, " e ", x2)