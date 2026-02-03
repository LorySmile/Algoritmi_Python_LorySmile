# Implementazione della ricerca lineare in Python

def linear_search(arr, target):

    """
    Esegue una ricerca lineare per trovare l'indice di target in arr.
    
    :param arr: Lista di elementi in cui cercare
    :param target: Elemento da cercare
    :return: Indice di target se trovato, altrimenti -1

    """

    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Restituisce l'indice se l'elemento è trovato
    return -1  # Restituisce -1 se l'elemento non è trovato

# Esempio di utilizzo
arr = [10, 23, 45, 70, 11, 15]
target = 70 
result = linear_search(arr, target)
print(result)                                 # Output: 3

# Spiegazione:
# 1. La funzione linear_search prende una lista arr e un elemento target come input.
# 2. Scorre ogni elemento della lista confrontandolo con target.
# 3. Se trova l'elemento, restituisce il suo indice.
# 4. Se l'elemento non viene trovato dopo aver controllato tutti gli elementi, restituisce -1.

# Complessità temporale: O(n), dove n è il numero di elementi nell'array.
# Complessità spaziale: O(1), poiché non utilizza spazio aggiuntivo significativo.

# La ricerca lineare è semplice da implementare e funziona bene per piccoli dataset 
# o liste non ordinate. Tuttavia, per liste grandi o ordinate, algoritmi più efficienti 
# come la ricerca binaria sono preferibili.

# La ricerca lineare può essere utilizzata con qualsiasi tipo di dati,
# inclusi numeri, stringhe e oggetti personalizzati, purché sia possibile confrontarli.
# Inoltre, la ricerca lineare è stabile, poiché non altera l'ordine degli elementi uguali.

# Tuttavia, non è il metodo più efficiente per dataset di grandi dimensioni.
# In tali casi, è consigliabile utilizzare algoritmi di ricerca più avanzati.
# come la ricerca binaria o strutture dati come alberi di ricerca bilanciati.

# In pratica, la scelta dell'algoritmo di ricerca dipende 
# dalle caratteristiche specifiche del dataset e dai requisiti di prestazione.
# separando i numeri negativi e positivi, 
# ordinandoli separatamente e poi combinandoli alla fine. 