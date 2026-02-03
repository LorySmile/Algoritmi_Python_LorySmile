# Verificare se un nodo è una foglia in un albero non binario.

def is_leaf(tree, nodo):
    return len(tree[nodo]) == 0        # una foglia non ha figli

# Esempio di utilizzo
non_binary_tree = {
    'A': {},
    'B': {'C': 1, 'D': 1},
    'C': {},
    'D': {}
}

nodo = 'A'
print("Il nodo  ", nodo, "è una foglia???", is_leaf(non_binary_tree, nodo))  # Output: Il nodo A è una foglia? True
nodo = 'B'
print("Il nodo  ", nodo, "è una foglia??", is_leaf(non_binary_tree, nodo))  # Output: Il nodo B è una foglia? False
nodo = 'C'
print("Il nodo ", nodo, "è una foglia?", is_leaf(non_binary_tree, nodo))  # Output: Il nodo C è una foglia? True

# Spiegazione:
# 1. La funzione is_leaf prende un albero rappresentato come dizionario e un nodo come input.
# 2. Controlla se il numero di figli del nodo è zero.
# 3. Restituisce True se il nodo è una foglia, altrimenti restituisce False.

# Complessità temporale: O(1), poiché l'operazione di controllo della lunghezza è costante.
# Complessità spaziale: O(1), poiché utilizza spazio costante.

# Una foglia è definita come un nodo che non ha figli.

# Si può anche scrivere in modo ricorsivo: ________________________________________________

def is_leaf_recursive(tree, nodo):
    if nodo not in tree:
        return False                  # caso base: nodo non esistente
    if len(tree[nodo]) == 0:
        return True                   # è una foglia
    return False                      # non è una foglia

# Esempio di utilizzo
nodo = 'D'
print("Il nodo ", nodo, "è una foglia?", is_leaf_recursive(non_binary_tree, nodo))  # Output: Il nodo D è una foglia? True

# Spiegazione:
# 1. La funzione is_leaf_recursive prende un albero rappresentato come dizionario e un nodo come input.
# 2. Se il nodo non esiste nell'albero, restituisce False (caso base).
# 3. Se il numero di figli del nodo è zero, restituisce True (è una foglia).
# 4. Altrimenti, restituisce False (non è una foglia).  

# Complessità temporale: O(1), poiché l'operazione di controllo della lunghezza è costante.
# Complessità spaziale: O(1), poiché utilizza spazio costante.

# Si può anche scrivere per alberi binari: ________________________________________________

def is_leaf(tree, nodo):
    return tree[nodo]['left'] is None and tree[nodo]['right'] is None

# Esempio di utilizzo
binary_tree = {
    'A': {'left': 'B', 'right': 'C'},
    'B': {'left': None, 'right': None},
    'C': {'left': None, 'right': None}
}

nodo = 'B'
print("Il nodo", nodo, "è una foglia nell'albero binario?", is_leaf(binary_tree, nodo))  # Output: Il nodo B è una foglia nell'albero binario? True
nodo = 'A'
print("Il nodo", nodo, "è una foglia nell'albero binario?", is_leaf(binary_tree, nodo))  # Output: Il nodo A è una foglia nell'albero binario? False

# Spiegazione:
# 1. La funzione is_leaf prende un albero binario rappresentato come dizionario
# 2. Controlla se i figli sinistro e destro del nodo sono entrambi None.
# 3. Restituisce True se il nodo è una foglia, altrimenti restituisce False.

# Complessità temporale: O(1), poiché l'operazione di controllo è costante.
# Complessità spaziale: O(1), poiché utilizza spazio costante.