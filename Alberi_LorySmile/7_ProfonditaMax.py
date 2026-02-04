# Calcolare la profondità massima di un albero non binario.

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
    if nodo not in tree:
        return -1
    if not tree[nodo]:          # nodo foglia
        return 0
    return 1 + max(altezza_non_binario(tree, child) for child in tree[nodo])

def trova_radice(tree):
    figli = set()
    for lista_figli in tree.values():
        figli.update(lista_figli)
    for nodo in tree:
        if nodo not in figli:
            return nodo

def profondita_max(tree):
    root = trova_radice(tree)
    return altezza_non_binario(tree, root)

print("Profondità massima albero non binario:", profondita_max(non_binary_tree))

# Spiegazione:
# 1. Trovo radice con trova_radice(tree);
# 2. Calcolo l'altezza del sottoalbero radicato in root usando la funzione altezza;
# 3. Restituisco il risultato.

# La complessità computazionale di profondita_max(tree) è O(n).

# Per alberi binari diventa: ________________________________________________________________

binary_tree = {
    'A': {'left': 'B', 'right': 'C', 'parent': None},
    'B': {'left': 'D', 'right': None, 'parent': 'A'},
    'C': {'left': None, 'right': None, 'parent': 'A'},
    'D': {'left': None, 'right': None, 'parent': 'B'}
}

def altezza_binario(tree, nodo):
    if nodo is None:
        return -1
    left = tree[nodo]['left']
    right = tree[nodo]['right']
    return 1 + max(altezza_binario(tree, left), altezza_binario(tree, right))

def trova_radice_binario(tree):
    for nodo in tree:
        if tree[nodo]['parent'] is None:
            return nodo

def profondita_max_binario(tree):
    root = trova_radice_binario(tree)
    return altezza_binario(tree, root)

print("Profondità massima albero binario:", profondita_max_binario(binary_tree))

# Scorro tutti i nodi e restituisco quello che non ha un padre, che per definizione è la radice dell’albero.

# Altezza e profondità massima coincidono solo se parti dalla radice

# Complessità: 
# - tempo:  O(n) 
# - spazio: O(h) per la ricorsione (h = altezza)