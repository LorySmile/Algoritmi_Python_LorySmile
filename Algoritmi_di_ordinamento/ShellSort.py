# Implementazione dell'algoritmo ShellSort in Python

def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Inizializza il gap

    # Continua a ridurre il gap fino a quando non diventa 0
    while gap > 0:
        # Esegui un'inserzione sort per questo gap
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Sposta gli elementi di arr[0..i-gap] che sono maggiori di temp
            # verso destra di gap posizioni
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        
        gap //= 2  # Riduci il gap

    return arr

# Esempio di utilizzo
if __name__ == "__main__":
    sample_array = [12, 34, 54, 2, 3]
    print("Array originale:", sample_array)
    sorted_array = shell_sort(sample_array)
    print("Array ordinato:", sorted_array)
    # Output: Array ordinato: [2, 3, 12, 34, 54]

    # Spiegazione:
    # 1. La funzione shell_sort prende una lista arr come input.
    # 2. Inizializza un gap a metà della lunghezza dell'array.
    # 3. Esegue un'inserzione sort per ogni elemento a intervalli di gap.
    # 4. Riduce il gap e ripete il processo fino a quando il gap non diventa 0.
    # 5. Alla fine, l'array risulta ordinato.
    # Complessità temporale: O(n^(3/2)) nel caso medio e peggiore,
    #                        O(n log n) nel caso migliore.
    # Complessità spaziale: O(1), poiché l'ordinamento avviene in loco.

    # ShellSort è un miglioramento dell'inserzione sort e
    # funziona bene per array di medie dimensioni.

    # Tuttavia, non è stabile, poiché può cambiare l'ordine degli elementi uguali.
    # La scelta della sequenza di gap può influenzare significativamente
    # le prestazioni dell'algoritmo.
    
    # In pratica, ShellSort è spesso più veloce di altri algoritmi di ordinamento
    # come Bubble Sort o Insertion Sort, specialmente per array di dimensioni maggiori
    # ed è semplice da implementare.