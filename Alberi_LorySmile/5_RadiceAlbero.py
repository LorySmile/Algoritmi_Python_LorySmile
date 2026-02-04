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
print("La radice dell'albero non binario (sapendo i padri) è", radice)  # Output: La radice dell'albero è A

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

# Se non ho il padre, trova_radice, per un albero non binario, sarà: ____________________________________________

non_binary_tree_1 = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

def altezza_non_binario_f(non_binary_tree_1, nodo):
    if nodo not in non_binary_tree_1:
        return -1
    if not non_binary_tree_1[nodo]:          # nodo foglia
        return 0
    return 1 + max(altezza_non_binario_f(non_binary_tree_1, child) for child in non_binary_tree_1[nodo])

def trova_radice_f(non_binary_tree_1):
    figli = set()
    for lista_figli in non_binary_tree_1.values():
        figli.update(lista_figli)
    for nodo in non_binary_tree_1:
        if nodo not in figli:
            return nodo

# Esempio di utilizzo
radice_non_binario = trova_radice_f(non_binary_tree_1)
print("La radice dell'albero non binario (per figli) è", radice_non_binario)  # Output: La radice dell'albero binario è A



