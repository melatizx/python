i = 0
imp = []
par = []
for n in range(i, 10):
  n = int(input(f"Digite o {i + 1}º numero: "))
  if n%2==0:
    imp.append(n)
  else:
    par.append(n)
  i = i+1
print(imp)
print(par)