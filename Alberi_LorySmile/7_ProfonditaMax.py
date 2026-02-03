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
    if nodo is None or nodo not in tree:
        return -1       # caso base: nodo nullo o non esistente
    if not tree[nodo]:  # se il nodo non ha figli
        return 0
    max_height = -1
    for child in tree[nodo]:
        max_height = max(max_height, altezza_non_binario(tree, child))
    return 1 + max_height

def trova_radice(tree):
    for nodo in tree:
        if tree[nodo]['parent'] is None:           
            return nodo         


# Profondità Massima

def profondita_max(tree):
    root = trova_radice(tree)
    return altezza_non_binario(tree, root)

# Spiegazione:
# 1. Trovo radice con trova_radice(tree);
# 2. Calcolo l'altezza del sottoalbero radicato in root usando la funzione altezza;
# 3. Restituisco il risultato.

# La complessità computazionale di profondita_max(tree) è O(n).

# Per alberi binari diventa: ________________________________________

binary_tree = {
    'A': {'left': 'B', 'right': 'C', 'parent': None},
    'B': {'left': 'D', 'right': None, 'parent': 'A'},
    'C': {'left': None, 'right': None, 'parent': 'A'},
    'D': {'left': None, 'right': None, 'parent': 'B'}
}
# L’albero è binario perché ogni nodo ha al più due figli, ma mantiene anche il riferimento al padre, 
# che permette di individuare la radice e calcolare la profondità risalendo l’albero.

def altezza_binario(tree, nodo):
    if nodo is None:
        return -1                                   # caso base: nodo nullo
    left = tree[nodo]['left']                       # è un dizionario che rappresenta l'albero
    right = tree[nodo]['right']                     # accediamo ai figli sinistro e destro
    return 1 + max(altezza_binario(tree, left), altezza_binario(tree, right))

def trova_radice_binario(tree):
    for nodo in tree:
        if tree[nodo]['parent'] is None:
            return nodo      

# Profondità Massima con albero binario:

def profondita_max(tree):
    radice = trova_radice_binario(tree)
    return altezza_binario(tree, radice)

# Scorro tutti i nodi e restituisco quello che non ha un padre, che per definizione è la radice dell’albero.

