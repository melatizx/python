dia_comeco = int(input().split()[1])
hora_comeco, minuto_comeco, segundo_comeco = map(int, input().split(' : '))
dia_final = int(input().split()[1])
hora_final, minuto_final, segundo_final = map(int, input().split(' : '))
duracao_segundos = ((dia_final - dia_comeco) * 24 * 60 * 60) + \
                   ((hora_final - hora_comeco) * 60 * 60) + \
                   ((minuto_final - minuto_comeco) * 60) + \
                   (segundo_final - segundo_comeco)
dias = duracao_segundos // (24 * 60 * 60)
horas = (duracao_segundos % (24 * 60 * 60)) // (60 * 60)
minutos = (duracao_segundos % (60 * 60)) // 60
segundos = duracao_segundos % 60
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")