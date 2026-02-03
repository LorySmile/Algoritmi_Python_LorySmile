# Implementazione dell'algoritmo BubbleSort in Python

def bubble_sort(arr):
    n = len(arr)
    # Ciclo attraverso tutti gli elementi dell'array
    for i in range(n):
        # Flag per verificare se è avvenuto uno scambio
        swapped = False
        # Ultimi i elementi sono già ordinati, quindi non li consideriamo
        for j in range(0, n - i - 1):
            # Confronta l'elemento corrente con il successivo
            if arr[j] > arr[j + 1]:
                # Scambia se l'elemento corrente è maggiore del successivo
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Se non ci sono stati scambi, l'array è già ordinato
        if not swapped:
            break
    return arr

# Esempio di utilizzo
if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(sample_array)
    print("Array ordinato:", sorted_array)
# Output atteso: Array ordinato: [11, 12, 22, 25, 34, 64, 90]

# Spiegazione dell'algoritmo:
# 1. L'algoritmo confronta ogni coppia di elementi adiacenti nell'array.
# 2. Se il primo elemento è maggiore del secondo, li scambia.
# 3. Questo processo viene ripetuto fino a quando l'intero array è ordinato.
# 4. L'ottimizzazione con il flag 'swapped' 
# permette di terminare l'algoritmo prima se l'array è già ordinato.

# Complessità temporale: O(n^2) nel caso peggiore e medio, 
#                        O(n) nel caso migliore (quando l'array è già ordinato).
# Complessità spaziale:  O(1) poiché l'algoritmo modifica l'array originale in-place.

# Vantaggi: Semplice da implementare e comprendere.
# Svantaggi: Non è efficiente per grandi dataset
# rispetto ad altri algoritmi di ordinamento come QuickSort o MergeSort.

# Note: BubbleSort è un algoritmo stabile,
# il che significa che preserva l'ordine relativo degli elementi uguali.
# Tuttavia, è raramente usato in pratica a causa della sua inefficienza.
# Può essere utile per piccoli dataset o come parte di algoritmi più complessi.

# Può essere utilizzato anche per ordinamenti parziali,
# come trovare i primi k elementi più piccoli in un array.

# In questo caso, l'algoritmo può essere interrotto dopo k iterazioni.

def bubble_sort_partial(arr, k):
    n = len(arr)
    for i in range(min(k, n)):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr[:k]

# Esempio di utilizzo per ordinamento parziale

sample_array_partial = [64, 34, 25, 12, 22, 11, 90]
k = 3
top_k_elements = bubble_sort_partial(sample_array_partial, k)
print(f"I primi {k} elementi più piccoli sono:", top_k_elements)
# Output atteso: I primi 3 elementi più piccoli sono: [11, 12, 22]

# Questa funzione ordina solo i primi k elementi dell'array
# utilizzando l'algoritmo BubbleSort e restituisce questi elementi ordinati.