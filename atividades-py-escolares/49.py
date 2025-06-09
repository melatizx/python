i = 3
n1 = 1
n2 = 1
n3 = 0
posi = int(input("Informe a posição que deseja saber: "))
while i<=posi:
  n3=n1+n2
  n1=n2
  n2=n3
  i=i+1
print(f"O numero é {n3}")