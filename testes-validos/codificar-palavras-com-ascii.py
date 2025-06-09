#Solicitaram para que você construisse um programa simples de criptografia. Este programa deve possibilitar enviar mensagens codificadas sem que alguém consiga lê-las. O processo é muito simples. São feitas três passadas em todo o texto.
#Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim sucessivamente. Na segunda passada, a linha deverá ser invertida. Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.
#Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”. O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.

saida_criptografia = []
i = 0
while True:
  N = int(input(""))
  if N >= 1 and N <= 10000:
    break

while i < N:
  palavra = input("")
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
