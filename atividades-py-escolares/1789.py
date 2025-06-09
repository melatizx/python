while True:
    try:
        # Lê o número de lesmas
        grupo = int(input())
        # Lê as velocidades das lesmas
        lesma_entrada = input().split()
        
        # Converte as velocidades para inteiros
        lesmas = [int(velocidade) for velocidade in lesma_entrada[:grupo]]
        
        # Encontra a maior velocidade
        maior = max(lesmas)
        
        # Determina o nível da lesma mais veloz
        if maior < 10:
            print("1")
        elif 10 <= maior < 20:
            print("2")
        else:  # maior >= 20
            print("3")
    except EOFError:
        break