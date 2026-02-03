# Implementazione dell'algoritmo SelectionSort in Python

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Trova l'indice del minimo elemento nell'array non ordinato
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Scambia il minimo elemento trovato con il primo elemento non ordinato
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Esempio di utilizzo
if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11]
    sorted_array = selection_sort(sample_array)
    print("Array ordinato:", sorted_array) 
# Output atteso: Array ordinato: [11, 12, 22, 25, 64]

# Spiegazione dell'algoritmo:
# 1. L'algoritmo divide l'array in due parti: la parte ordinata e la parte non ordinata.
# 2. In ogni iterazione, trova il minimo elemento nella parte non ordinata.
# 3. Scambia questo minimo elemento con il primo elemento della parte non ordinata.
# 4. Ripete il processo fino a quando l'intero array è ordinato.

# Complessità temporale: O(n^2) nel caso peggiore e medio e nel caso migliore.
# Complessità spaziale: O(1) poiché l'algoritmo modifica l'array originale in-place.

# Vantaggi: Semplice da implementare e comprendere.
# Svantaggi: Non è efficiente per grandi dataset 
# rispetto ad altri algoritmi di ordinamento come QuickSort o MergeSort.

# Note: SelectionSort non è un algoritmo stabile, 
# il che significa che non preserva l'ordine relativo degli elementi uguali.
# Tuttavia, è utile quando la memoria è limitata poiché richiede spazio aggiuntivo minimo.

# Può essere utilizzato anche per ordinamenti parziali, 
# come trovare i primi k elementi più piccoli in un array.
# In questo caso, l'algoritmo può essere interrotto dopo k iterazioni.

# Ad esempio, per trovare i primi 3 elementi più piccoli:

def selection_sort_partial(arr, k):
    n = len(arr)
    for i in range(min(k, n)):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr[:k]

# Esempio di utilizzo per ordinamento parziale

sample_array_partial = [64, 25, 12, 22, 11]
k = 3
top_k_elements = selection_sort_partial(sample_array_partial, k)
print(f"I primi {k} elementi più piccoli sono:", top_k_elements)

# Output atteso: I primi 3 elementi più piccoli sono: [11, 12, 22]

# Questo dimostra la flessibilità dell'algoritmo SelectionSort per vari scenari di ordinamento.