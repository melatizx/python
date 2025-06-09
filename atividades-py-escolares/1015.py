import math
i = 0
c = 0
p1 = []
p2 = []
entrada= input()
x1, y1 = entrada.split()
entrada= input()
x2, y2 = entrada.split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

resultado = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f'{resultado:.4f}')