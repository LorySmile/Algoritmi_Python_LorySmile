# Quanti percorsi diversi ci sono da un angolo a quello opposto di un traliccio 20x20?

def fattoriale(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
n = 20
percorsi = fattoriale(2 * n) // (fattoriale(n) * fattoriale(n))
print(percorsi)  # il numero di percorsi è 137846528820

# Spiegazione: Il numero di percorsi in un traliccio n x n è dato dal coefficiente binomiale C(2n, n),
# che rappresenta il numero di modi per scegliere n movimenti verso il basso (o verso destra) in un totale di 2n movimenti. 
# La formula per C(2n, n) è (2n)! / (n! * n!), calcolata qui usando la funzione fattoriale definita sopra.  
# Per un traliccio 20x20, n è 20, quindi calcoliamo C(40, 20) per ottenere il numero di percorsi distinti.  
# Il risultato finale è 137846528820.