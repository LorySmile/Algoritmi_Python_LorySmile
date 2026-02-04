# Verificare se due nodi sono fratelli.
# Due nodi sono fratelli se e solo se hanno lo stesso padre.

# Albero non binario

tree = {
    'A': {'children': ['B', 'C'], 'parent': None},
    'B': {'children': ['D'], 'parent': 'A'},
    'C': {'children': [], 'parent': 'A'},
    'D': {'children': [], 'parent': 'B'}
}

# Albero binario

binary_tree = {
    'A': {'left': 'B', 'right': 'C', 'parent': None},
    'B': {'left': None, 'right': None, 'parent': 'A'},
    'C': {'left': None, 'right': None, 'parent': 'A'}
}

# Funzione che controlla se a e b sono fratelli per l'albero non binario: ____________________________________

def sono_fratelli(tree, a, b):
    if a not in tree or b not in tree:              # così non va in errore se uno dei nodi non esiste
        return False
    if a == b:                                      # così non considera fratelli anche un nodo con sè stesso 
        return False                                
    return tree[a]['parent'] == tree[b]['parent']   

# Funzione che controlla se a e b sono fratelli per l'albero binario: _________________________________________

def sono_fratelli(binary_tree, a, b):
    if a not in binary_tree or b not in binary_tree:              # così non va in errore se uno dei nodi non esiste
        return False
    if a == b:                                      # così non considera fratelli anche un nodo con sè stesso 
        return False                                
    return binary_tree[a]['parent'] == binary_tree[b]['parent']   

# E' un controllo in tempo costante O(1).

