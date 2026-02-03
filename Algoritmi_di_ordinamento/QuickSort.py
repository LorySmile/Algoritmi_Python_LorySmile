# Implementazione dell'algoritmo QuickSort in Python

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    
# Esempio di utilizzo
arr = [3,6,8,10,1,2,1]
print(quicksort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]

# Spiegazione:
# 1. La funzione quicksort prende in input una lista 'arr'.
# 2. Se la lista ha 1 o 0 elementi, viene restituita tale lista (caso base).
# 3. Altrimenti, viene scelto un pivot (elemento centrale della lista).
# 4. La lista viene divisa in tre parti: elementi minori del pivot, elementi uguali al pivot e elementi maggiori del pivot.
# 5. La funzione si chiama ricorsivamente sulle liste di sinistra e destra, e concatena i risultati con la lista del pivot.
# 6. Infine, viene restituita la lista ordinata.

# Complessità temporale media: O(n log n), peggiore caso: O(n^2)
# Complessità spaziale: O(log n) per la profondità della ricorsione
# Nota: Questa implementazione utilizza spazio aggiuntivo per le liste left, middle e right.
# Tuttavia, esistono versioni in-place di QuickSort che riducono l'uso di memoria.

# QuickSort è un algoritmo di ordinamento molto efficiente e ampiamente utilizzato
# in molte librerie standard di programmazione e framework 
# a causa della sua efficienza e versatilità.

# Viene spesso preferito ad altri algoritmi di ordinamento per la sua velocità e semplicità.
# Tuttavia, la scelta del pivot può influenzare significativamente le prestazioni.
# In questa implementazione, il pivot è scelto come l'elemento centrale della lista.

# In scenari reali, si possono adottare strategie più sofisticate per la scelta del pivot,
# come il "median-of-three" o la selezione casuale, 
# per migliorare le prestazioni in casi particolari.

# Inoltre, QuickSort è un algoritmo stabile solo se implementato con attenzione,
# poiché gli elementi uguali possono essere riordinati durante il processo di partizionamento
# a seconda dell'implementazione specifica.

# QuickSort è un algoritmo di ordinamento basato sulla tecnica "divide et impera".
# Funziona dividendo l'array in sotto-array più piccoli e ordinandoli ricorsivamente.
# La sua efficienza lo rende adatto per l'ordinamento di grandi dataset.

# Tuttavia, per dataset molto piccoli, 
# algoritmi come Insertion Sort possono essere più efficienti.
# In pratica, QuickSort viene spesso combinato con altri algoritmi di ordinamento 
# per ottimizzare le prestazioni complessive.
