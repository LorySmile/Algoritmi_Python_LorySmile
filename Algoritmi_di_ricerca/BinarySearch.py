# Implementazione della ricerca binaria in Python

def binary_search(arr, target):

    """
    Esegue una ricerca binaria per trovare l'indice di target in arr ordinato.
    
    :param arr: Lista ordinata di elementi in cui cercare
    :param target: Elemento da cercare
    :return: Indice di target se trovato, altrimenti -1

    """

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calcola l'indice medio

        # Controlla se target è presente al centro
        if arr[mid] == target:
            return mid  # Restituisce l'indice se l'elemento è trovato
        # Se target è maggiore, ignora la metà sinistra
        elif arr[mid] < target:
            left = mid + 1
        # Se target è minore, ignora la metà destra
        else:
            right = mid - 1

    return -1  # Restituisce -1 se l'elemento non è trovato

# Esempio di utilizzo
arr = [10, 15, 23, 45, 70, 85]
target = 70
result = binary_search(arr, target)
print(f"Elemento {target} trovato all'indice: {result}")
# Output: Elemento 70 trovato all'indice: 4

# Spiegazione:
# 1. La funzione binary_search prende una lista ordinata arr e un elemento target come input.
# 2. Inizializza due puntatori, left e right, per tracciare l'inizio e la fine dell'array.
# 3. Calcola l'indice medio e confronta l'elemento medio con target.
# 4. Se trova l'elemento, restituisce il suo indice.
# 5. Se target è maggiore dell'elemento medio, sposta il puntatore left a mid + 1.
# 6. Se target è minore, sposta il puntatore right a mid - 1.
# 7. Ripete il processo finché left non supera right.
# 8. Se l'elemento non viene trovato, restituisce -1.

# Complessità temporale: O(log n), dove n è il numero di elementi nell'array.
# Complessità spaziale: O(1), poiché non utilizza spazio aggiuntivo significativo.

# La ricerca binaria è molto efficiente per liste ordinate e riduce significativamente
# il numero di confronti necessari rispetto alla ricerca lineare.
# Tuttavia, richiede che l'array sia ordinato prima dell'esecuzione.

# La ricerca binaria può essere utilizzata con qualsiasi tipo di dati ordinabili,
# inclusi numeri e stringhe, purché sia possibile confrontarli.

# Tuttavia, non è adatta per liste non ordinate o per strutture dati che non supportano
# l'accesso casuale agli elementi, come le liste collegate.

# In pratica, la scelta dell'algoritmo di ricerca dipende 
# dalle caratteristiche specifiche del dataset e dai requisiti di prestazione.

# Per liste ordinate di grandi dimensioni, la ricerca binaria è generalmente preferibile
# rispetto alla ricerca lineare a causa della sua maggiore efficienza.

# Inoltre, la ricerca binaria può essere implementata in modo ricorsivo o iterativo,
# a seconda delle preferenze e dei requisiti specifici dell'applicazione.
# Entrambi gli approcci hanno complessità temporali simili, ma l'iterativo evita il sovraccarico
# della chiamata di funzione ricorsiva.

# Infine, è importante notare che la ricerca binaria non è stabile,
# poiché non garantisce l'ordine degli elementi uguali nell'array originale.
# Pertanto, se la stabilità è un requisito, è necessario considerare altre opzioni.
# In tali casi, è consigliabile utilizzare algoritmi di ricerca più avanzati
# come la ricerca lineare o strutture dati come alberi di ricerca bilanciati.