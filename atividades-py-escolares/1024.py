saida_criptografia = []
i = 0
while True:
  N = int(input("Numero de criptografias: "))
  if N >= 1 and N <= 10000:
    break

while i < N:
  palavra = input("Para criptografar: ")
  palavra_1etapa = []
  palavra_1etapa_exc = []
  palavra_final = []
  palavra_final_exc = []
  for l in palavra:
    if l.isalpha():
      cod = ord(l)
      cod2 = cod + 3
      letra_gerada = chr(cod2)
      palavra_1etapa.append(letra_gerada)
    else:
      palavra_1etapa.append(l)

  palavra_1 = palavra_1etapa

  palavra_2etapa = palavra_1[::-1]
  tamanho = int(len(palavra_2etapa) / 2)

  palavra_3etapa = palavra_2etapa[tamanho:]

  for c in palavra_3etapa:
    cod = ord(c)
    cod2 = cod - 1
    letra_gerada = chr(cod2)
    palavra_final.append(letra_gerada)

  parte_final = palavra_final
  palavra_cod = palavra_2etapa[0:tamanho] + parte_final
  palavraX = ''.join(palavra_cod)
  i = i + 1
  saida_criptografia.append(palavraX)

for saida in saida_criptografia:
  print(saida)