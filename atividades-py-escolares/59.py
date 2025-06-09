a = 80000
b = 200000
anos = 0
while a<=b:
  a2 = (a*3)/100
  a = a+a2
  b2 = (b*1.5)/100
  b = b+b2
  anos = anos+1
print(f"Levará {anos} anos para a cidade A ultrapassar a população da cidade B")