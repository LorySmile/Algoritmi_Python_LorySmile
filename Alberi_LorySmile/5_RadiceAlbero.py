# Calcolare la radice di un albero non binario.

non_binary_tree = {
    'A': {'parent': None},
    'B': {'parent': 'A'},
    'C': {'parent': 'A'},
    'D': {'parent': 'B'},
    'E': {'parent': 'B'},
    'F': {'parent': 'C'}
}

def trova_radice(tree):
    for nodo in tree:
        if tree[nodo]['parent'] is None:
            return nodo
        
# Esempio di utilizzo

radice = trova_radice(non_binary_tree)
print("La radice dell'albero è", radice)  # Output: La radice dell'albero è A

# Spiegazione:
# 1. La funzione trova_radice prende un albero rappresentato come dizionario come input.
# 2. Itera su tutti i nodi dell'albero.
# 3. Controlla se il parent del nodo è None.
# 4. Se trova un nodo con parent None, lo restituisce come radice.

# Complessità temporale: O(n), dove n è il numero di nodi nell'albero.
# Complessità spaziale: O(1), poiché utilizza spazio costante.

# La radice di un albero è il nodo principale da cui tutti gli altri nodi discendono.
# Questa funzione può essere utilizzata per analizzare strutture ad albero,
# come alberi binari di ricerca, alberi AVL, alberi rosso-neri, ecc.
# Può essere utile in vari algoritmi che richiedono la conoscenza della radice
# dell'albero, come traversamenti, bilanciamento degli alberi, ecc.

# Inoltre, può essere adattata per alberi binari modificando la struttura dati dell'albero.
# Ecco un albero binario come esempio: ___________________________________

binary_tree = {
    'A': {'left': 'B', 'right': 'C', 'parent': None},
    'B': {'left': 'D', 'right': None, 'parent': 'A'},
    'C': {'left': None, 'right': None, 'parent': 'A'},
    'D': {'left': None, 'right': None, 'parent': 'B'}
}

def trova_radice_binario(tree):
    for nodo in tree:
        if tree[nodo]['parent'] is None:
            return nodo
        
# Esempio di utilizzo
radice_binario = trova_radice_binario(binary_tree)
print("La radice dell'albero binario è", radice_binario)  # Output: La radice dell'albero binario è A

