import math

total_dias = int(input(""))

ano = total_dias // 365
resto_dias = total_dias % 365

mes = resto_dias // 30
dias = resto_dias % 30

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dias} dia(s)")
    