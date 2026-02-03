# Implementazione dell'algoritmo CountingSort in Python

def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Crea il conteggio degli elementi
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Memorizza il conteggio di ogni elemento
    for num in arr:
        count[num - min_val] += 1

    # Modifica il conteggio in modo che ogni elemento contenga la posizione finale
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Costruisci l'array di output
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# Esempio di utilizzo
arr = [3, 6, 8, 10, 1, 2, 1]
print(counting_sort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]

# Spiegazione:
# 1. La funzione counting_sort prende in input una lista 'arr'.
# 2. Trova il valore massimo e minimo nella lista per determinare l'intervallo degli elementi.
# 3. Crea un array di conteggio per ogni elemento nell'intervallo.
# 4. Conta le occorrenze di ogni elemento nella lista originale.
# 5. Modifica l'array di conteggio in modo che ogni elemento contenga la posizione finale.
# 6. Costruisce l'array di output in base ai conteggi e alle posizioni finali.
# 7. Restituisce l'array ordinato.

# Complessità temporale: O(n + k), dove n è il numero di elementi nella lista
# e k è l'intervallo degli elementi (max - min)
# Complessità spaziale: O(k) per l'array di conteggio e O(n) per l'array di output

# CountingSort è un algoritmo di ordinamento non comparativo
# che è particolarmente efficiente quando l'intervallo degli elementi (k)
# è non molto più grande del numero di elementi (n) da ordinare.

# Funziona bene per interi e può essere adattato per ordinare altri tipi di dati
# mappandoli a interi.  Tuttavia, non è adatto per dati con un intervallo molto grande
# rispetto al numero di elementi, poiché ciò comporterebbe un uso eccessivo di memoria.

# CountingSort è un algoritmo di ordinamento stabile,
# poiché mantiene l'ordine relativo degli elementi uguali durante il processo di ordinamento.

# Inoltre, CountingSort è spesso utilizzato come parte di altri algoritmi di ordinamento,
# come Radix Sort, per migliorare le prestazioni complessive su dataset specifici
# dove gli elementi possono essere rappresentati come interi.

# CountingSort è un algoritmo di ordinamento basato sul conteggio degli elementi.

# Non confronta gli elementi direttamente, ma utilizza il conteggio delle occorrenze
# per determinare la posizione di ciascun elemento nell'array ordinato.

# La sua efficienza lo rende adatto per l'ordinamento di grandi dataset
# con un intervallo limitato di valori.

# Tuttavia, per dataset con un intervallo molto grande,
# algoritmi come QuickSort o MergeSort possono essere più efficienti.

# In pratica, CountingSort viene spesso combinato con altri algoritmi di ordinamento
# per ottimizzare le prestazioni complessive.

# Nota: Questa implementazione di CountingSort utilizza spazio aggiuntivo
# per l'array di conteggio e l'array di output.
# Esistono varianti che cercano di ridurre l'uso di memoria,
# ma possono essere più complesse da implementare.
