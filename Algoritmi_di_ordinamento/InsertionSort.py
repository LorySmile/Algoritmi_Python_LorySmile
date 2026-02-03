# Implementazione dell'algoritmo InsertionSort in Python

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Esempio di utilizzo
arr = [3, 6, 8, 10, 1, 2, 1]
print(insertion_sort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]

# Spiegazione:
# 1. La funzione insertion_sort prende in input una lista 'arr'.
# 2. Si itera attraverso la lista a partire dal secondo elemento.
# 3. Per ogni elemento (key), si confronta con gli elementi precedenti
#    e si spostano gli elementi maggiori di key di una posizione a destra.
# 4. Quando si trova la posizione corretta, si inserisce key.
# 5. Alla fine, viene restituita la lista ordinata.

# Complessità temporale: O(n^2) nel caso peggiore, O(n) nel caso migliore (lista già ordinata)
# Complessità spaziale: O(1) poiché l'ordinamento avviene in loco

# InsertionSort è un algoritmo di ordinamento semplice ed efficiente
# per liste di piccole dimensioni o quasi ordinate.
# Funziona bene in scenari in cui la lista è parzialmente ordinata,
# poiché la complessità temporale si avvicina a O(n) in tali casi.
# Tuttavia, per liste di grandi dimensioni, algoritmi più efficienti 
# come MergeSort o QuickSort sono preferibili.

# InsertionSort è un algoritmo di ordinamento basato sul concetto
# di costruire gradualmente una lista ordinata, inserendo
# ogni nuovo elemento nella posizione corretta.
# La sua semplicità lo rende facile da implementare e comprendere.

# In pratica, InsertionSort viene spesso utilizzato 
# come parte di algoritmi di ordinamento più complessi,
# specialmente per ottimizzare le prestazioni su piccoli sottoinsiemi di dati.

# Nota: Questa implementazione di InsertionSort ordina la lista in loco,
# senza utilizzare spazio aggiuntivo significativo.

# InsertionSort è un algoritmo di ordinamento stabile,
# poiché mantiene l'ordine relativo degli elementi uguali durante il processo di ordinamento.

# Inoltre, InsertionSort è particolarmente utile
# in situazioni in cui i dati vengono ricevuti in streaming
# e devono essere ordinati man mano che arrivano,
# poiché può inserire nuovi elementi in una lista già ordinata con efficienza.

# InsertionSort è spesso utilizzato in combinazione con altri algoritmi di ordinamento
# per migliorare le prestazioni complessive, specialmente su dataset di piccole dimensioni.
# Ad esempio, può essere utilizzato per ordinare piccoli blocchi di dati
# all'interno di algoritmi più complessi come QuickSort o MergeSort.
# Questo approccio ibrido sfrutta i punti di forza di entrambi gli algoritmi.