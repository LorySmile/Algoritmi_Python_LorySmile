# Calcolare l'altezza di un nodo in un albero binario.

tree = {
    'A': {'left': 'B', 'right': 'C'},
    'B': {'left': 'D', 'right': None},
    'C': {'left': None, 'right': None},
    'D': {'left': None, 'right': None}
}

def altezza(tree, nodo):
    if nodo is None:
        return -1  # caso base: nodo nullo
    left = tree[nodo]['left']                       # è un dizionario che rappresenta l'albero
    right = tree[nodo]['right']                     # accediamo ai figli sinistro e destro
    return 1 + max(altezza(tree, left), altezza(tree, right))

# Esempio di utilizzo
nodo = 'B'
print("L'altezza del nodo", nodo, "è", altezza(tree, nodo))  # Output: L'altezza del nodo B è 1

# Spiegazione:
# 1. La funzione altezza prende un albero rappresentato come dizionario e un nodo come input.
# 2. Se il nodo è None, restituisce -1 (caso base). 
# 3. Altrimenti, ottiene i figli sinistro e destro del nodo.
# 4. Calcola ricorsivamente l'altezza dei figli sinistro e destro.
# 5. Restituisce 1 più il massimo delle altezze dei figli.

# Complessità temporale: O(n), dove n è il numero di nodi nell'albero.
# Complessità spaziale: O(h), dove h è l'altezza dell'albero a causa della profondità della ricorsione.

# L'altezza di un nodo è definita come il numero di archi nel percorso più lungo
# dalla radice del nodo fino a una foglia. Un nodo foglia ha altezza 0, 
# mentre un nodo nullo ha altezza -1.

# Questa funzione può essere utilizzata per analizzare strutture ad albero,
# come alberi binari di ricerca, alberi AVL, alberi rosso-neri, ecc.
# Può essere utile in vari algoritmi che richiedono la conoscenza dell'altezza dei nodi,
# come bilanciamento degli alberi, calcolo della profondità, ecc.

# Inoltre, può essere adattata per alberi non binari modificando la struttura dati dell'albero.
# La funzione può essere estesa per gestire alberi più complessi
# o per calcolare altre proprietà correlate ai nodi dell'albero.

# Ecco un albero non binario come esempio: ___________________________________

non_binary_tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}   

def altezza_non_binario(tree, nodo):
    if nodo is None or nodo not in tree:
        return -1       # caso base: nodo nullo o non esistente
    if not tree[nodo]:  # se il nodo non ha figli
        return 0
    max_height = -1
    for child in tree[nodo]:
        max_height = max(max_height, altezza_non_binario(tree, child))
    return 1 + max_height

# Esempio di utilizzo per albero non binario

nodo = 'B'
print("L'altezza del nodo", nodo, "nell'albero non binario è", altezza_non_binario(non_binary_tree, nodo))  # Output: L'altezza del nodo B nell'albero non binario è 1

# Spiegazione:
# 1. La funzione altezza_non_binario prende un albero non binario rappresentato come dizionario e un nodo come input.
# 2. Se il nodo è None o non esiste nell'albero, restituisce -1 (caso base).
# 3. Se il nodo non ha figli, restituisce 0.
# 4. Altrimenti, itera su tutti i figli del nodo, calcolando ricorsivamente la loro altezza.
# 5. Restituisce 1 più il massimo delle altezze dei figli.