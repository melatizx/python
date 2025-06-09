entrada= input()
a, b, c = entrada.split()

a = int(a)
b = int(b)
c = int(c)

maiorab = (a+b+abs(a-b))/2

if maiorab > c:
    print(f'{maiorab:.0f} eh o maior')
else:
    print(f'{c:.0f} eh o maior')