# Implementazione dell'algoritmo RadixSort in Python

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Base 10 per cifre decimali

    # Conta le occorrenze delle cifre
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Modifica count[i] in modo che contenga la posizione effettiva di questa cifra in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Costruisci l'array output
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copia l'array output in arr[], in modo che arr[] ora contenga i numeri ordinati secondo la cifra corrente
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Trova il numero massimo per sapere il numero di cifre
    max1 = max(arr)

    # Applica counting sort per ogni cifra
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# Esempio di utilizzo
arr = [170, 45, 75, 90, 802, 242, 66]
radix_sort(arr)
print(arr)          # Output: [45, 66, 75, 90, 170, 242, 802]

# Spiegazione:
# 1. La funzione counting_sort_for_radix ordina l'array in base alla cifra rappresentata da exp (1 per le unità, 10 per le decine, ecc.).
# 2. La funzione radix_sort trova il numero massimo nell'array per determinare il numero di cifre.
# 3. Per ogni cifra, chiama counting_sort_for_radix per ordinare l'array in base a quella cifra.
# 4. Alla fine, l'array risulta ordinato.

# Complessità temporale: O(d * (n + k)), dove d è il numero di cifre nel numero più grande, 
#             n è il numero di elementi nell'array e k è la base (10 per i numeri decimali).
# Complessità spaziale: O(n + k) per l'array di output e l'array di conteggio.

# RadixSort è particolarmente efficiente per ordinare numeri interi 
# e può essere utilizzato anche per ordinare stringhe.
# Tuttavia, non è un algoritmo di ordinamento comparativo e
# la sua efficienza dipende dalla distribuzione dei dati e dal numero di cifre.

# RadixSort è stabile se il Counting Sort utilizzato come sottoprocedura è stabile.
# Inoltre, RadixSort è adatto per l'ordinamento di grandi dataset
# e può essere più veloce di algoritmi come QuickSort o MergeSort in determinate situazioni.

# Tuttavia, per dataset molto piccoli,
# algoritmi come Insertion Sort possono essere più efficienti.

# In pratica, RadixSort viene spesso combinato con altri algoritmi di ordinamento
# per ottimizzare le prestazioni complessive.

# Ad esempio, si può utilizzare RadixSort per grandi dataset
# e passare a Insertion Sort per piccoli sotto-array.
# Ciò consente di sfruttare i punti di forza di entrambi gli algoritmi.
# Questo approccio ibrido può migliorare significativamente 
# le prestazioni complessive dell'ordinamento.

# Inoltre, RadixSort può essere parallelizzato facilmente,
# rendendolo adatto per l'elaborazione su larga scala in ambienti distribuiti.
# Ciò lo rende una scelta popolare per l'ordinamento 
# di grandi quantità di dati in applicazioni moderne.

# Infine, RadixSort è ampiamente utilizzato in applicazioni come
# l'ordinamento di numeri di telefono, codici postali e altri dati numerici
# dove la velocità e l'efficienza sono cruciali.

# Nota: RadixSort funziona meglio con numeri interi non negativi.
# Per gestire numeri negativi, è possibile adattare l'algoritmo
# separando i numeri negativi e positivi, ordinandoli separatamente e poi combinandoli alla fine.

# RadixSort è un algoritmo di ordinamento basato sulla tecnica "distribuzione".
# Funziona ordinando i numeri cifra per cifra, partendo dalla cifra meno significativa
# fino alla cifra più significativa.