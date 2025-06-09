n = int(input())
dentro = 0
fora = 0
if n <10000:
    for x in range(n):
        x = int(input())
        if x>=10 and x<=20:
            dentro = dentro+1
        else:
            fora = fora+1
print(f"{dentro} in")
print(f"{fora} out")