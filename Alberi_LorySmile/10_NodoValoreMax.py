# Trovare il nodo con il valore massimo (se i valori sono nei nodi)

# Caso 1 - Il valore è nel nodo - Chiave -> Valore Numerico ____________________________________

tree = {
    'A': {'value': 10, 'children': ['B', 'C']},
    'B': {'value': 42, 'children': ['D']},
    'C': {'value': 7,  'children': []},
    'D': {'value': 30, 'children': []}
}

def nodo_valore_massimo(tree):         # DFS completa
    max_nodo = None
    max_valore = float('-inf')

    for nodo in tree:
        valore = tree[nodo]['value']
        if valore > max_valore:
            max_valore = valore
            max_nodo = nodo
                                        # Non serve nemmeno sapere qual è la radice
    return max_nodo, max_valore         # Output: ('B', 42)   

# Complessità:
# Tempo: O(n)
# Spazio: O(1)

# Caso 2 - Valore Massimo visitando l'albero (DFS) ________________________________________

def max_nodo_dfs(tree, nodo):
    max_nodo = nodo
    max_valore = tree[nodo]['value']

    for figlio in tree[nodo]['children']:
        candidato, valore = max_nodo_dfs(tree, figlio)
        if valore > max_valore:
            max_nodo = candidato
            max_valore = valore

    return max_nodo, max_valore

radice = 'A'
print(max_nodo_dfs(tree, radice))

# Tempo:  O(n)
# Spazio: O(h) (stack ricorsivo)

# Caso 3 - Albero Binario con valore nel nodo (con funzione ricorsiva)

binary_tree = {
    'A': {'value': 10, 'left': 'B', 'right': 'C'},
    'B': {'value': 5,  'left': None, 'right': None},
    'C': {'value': 20, 'left': None, 'right': None}
}

def max_binario(tree, nodo):
    if nodo is None:
        return None, float('-inf')

    nodo_sx, val_sx = max_binario(tree, tree[nodo]['left'])
    nodo_dx, val_dx = max_binario(tree, tree[nodo]['right'])

    max_nodo = nodo
    max_val = tree[nodo]['value']

    if val_sx > max_val:
        max_nodo, max_val = nodo_sx, val_sx
    if val_dx > max_val:
        max_nodo, max_val = nodo_dx, val_dx

    return max_nodo, max_val

# Se l’albero NON è un BST, trovare il massimo richiede visitare tutti i nodi.
# Quindi Ω(n) è un limite inferiore inevitabile.

# Se fosse un Binary Search Tree, il massimo sarebbe:
# il nodo più a destra → O(h)