# Implementazione dell'algoritmo MergeSort in Python

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])

    return sorted_array

# Esempio di utilizzo
arr = [3, 6, 8, 10, 1, 2, 1]
print(merge_sort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]

# Spiegazione:
# 1. La funzione merge_sort prende in input una lista 'arr'.
# 2. Se la lista ha 1 o 0 elementi, viene restituita tale lista (caso base).
# 3. Altrimenti, la lista viene divisa in due metà.
# 4. La funzione si chiama ricorsivamente su entrambe le metà.
# 5. La funzione merge unisce le due metà ordinate in un'unica lista ordinata.
# 6. Infine, viene restituita la lista ordinata.

# Complessità temporale: O(n log n) in tutti i casi (migliore, medio, peggiore)
# Complessità spaziale: O(n) a causa dell'uso di spazio aggiuntivo per le liste temporanee

# MergeSort è un algoritmo di ordinamento stabile e molto efficiente
# per grandi dataset, ed è spesso utilizzato in applicazioni pratiche.
# Funziona bene con strutture di dati che non supportano l'accesso casuale,
# come le liste collegate, e può essere facilmente parallelizzato per migliorare le prestazioni.
# Tuttavia, a causa del suo uso di spazio aggiuntivo, potrebbe non essere la scelta migliore
# per sistemi con memoria limitata.

# MergeSort è un algoritmo di ordinamento basato sulla tecnica "divide et impera".
# Funziona dividendo l'array in sotto-array più piccoli e ordinandoli ricorsivamente.
# La sua efficienza lo rende adatto per l'ordinamento di grandi dataset.
# Tuttavia, per dataset molto piccoli,
# algoritmi come Insertion Sort possono essere più efficienti.
# In pratica, MergeSort viene spesso combinato con altri algoritmi di ordinamento
# per ottimizzare le prestazioni complessive.

# Nota: Questa implementazione di MergeSort utilizza spazio aggiuntivo
# per le liste temporanee durante il processo di fusione.
# Esistono versioni in-place di MergeSort che riducono l'uso di memoria,
# ma sono più complesse da implementare.

# Inoltre, MergeSort è un algoritmo stabile,
# poiché mantiene l'ordine relativo degli elementi uguali durante il processo di fusione.
# Questa caratteristica lo rende particolarmente utile in scenari in cui la stabilità è importante.

# Infine, MergeSort è spesso utilizzato in librerie standard di programmazione
# e framework a causa della sua efficienza e stabilità.