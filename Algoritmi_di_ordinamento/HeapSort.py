# Implementazione dell'algoritmo HeapSort in Python

def heapify(arr, n, i):
    largest = i  # Inizializza il più grande come radice
    left = 2 * i + 1     
    right = 2 * i + 2    

    # Vedi se il figlio sinistro della radice esiste ed è maggiore della radice
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Vedi se il figlio destro della radice esiste ed è maggiore della radice
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Cambia la radice, se necessario
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # scambia

        # Heapify la radice.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Costruisci un maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Uno per uno estrae gli elementi dal heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # scambia
        heapify(arr, i, 0)
    return arr

# Esempio di utilizzo
arr = [3, 6, 8, 10, 1, 2, 1]
print(heap_sort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]

# Spiegazione:
# 1. La funzione heap_sort prende in input una lista 'arr'.
# 2. Si costruisce un maxheap dalla lista.
# 3. Si estrae l'elemento massimo (la radice del heap) e lo si mette alla fine della lista.
# 4. Si riduce la dimensione del heap di uno e si heapifica la radice.
# 5. Si ripete il processo fino a quando tutti gli elementi sono estratti e la lista è ordinata.
# 6. Infine, viene restituita la lista ordinata.

# Complessità temporale: O(n log n) in tutti i casi (migliore, medio, peggiore)
# Complessità spaziale: O(1) poiché l'ordinamento avviene in loco

# HeapSort è un algoritmo di ordinamento efficiente e in loco
# che utilizza una struttura dati chiamata heap per ordinare gli elementi.
# Funziona bene per grandi dataset e non richiede spazio aggiuntivo significativo.

# Tuttavia, HeapSort non è un algoritmo stabile,
# poiché l'ordine relativo degli elementi uguali potrebbe non essere mantenuto.
# HeapSort è un algoritmo di ordinamento basato sulla tecnica "heap".
# Funziona costruendo un heap dalla lista e poi estraendo gli elementi in ordine ordinato.

# La sua efficienza lo rende adatto per l'ordinamento di grandi dataset.
# Tuttavia, per dataset molto piccoli,
# algoritmi come Insertion Sort possono essere più efficienti.

# In pratica, HeapSort viene spesso combinato con altri algoritmi di ordinamento
# per ottimizzare le prestazioni complessive.

# Nota: Questa implementazione di HeapSort ordina la lista in loco,
# senza utilizzare spazio aggiuntivo significativo.
