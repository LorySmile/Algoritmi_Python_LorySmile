# Trovare la somma dei numeri lungo le diagonali di una spirale 1001x1001.

dimensione = 1001
somma_diagonali = 1                   # Inizializza con il centro della spirale
numero = 1                            # Inizia dal numero 1 al centro della spirale   

for livello in range(1, (dimensione // 2) + 1):
    passo = livello * 2               # La distanza tra i numeri diagonali aumenta di 2 per ogni livello
    for _ in range(4):                # Ci sono 4 numeri diagonali per ogni livello
        numero += passo
        somma_diagonali += numero

print(somma_diagonali)                # La somma delle diagonali è 669171001