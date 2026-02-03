# Calcolare il numero di foglie in un albero binario.

tree = {
    'A': {'left': 'B', 'right': 'C'},
    'B': {'left': 'D', 'right': None},
    'C': {'left': None, 'right': None},
    'D': {'left': None, 'right': None}
}

def conta_foglie(tree, nodo):
    if nodo is None:
        return 0                   # caso base: nodo nullo
    left = tree[nodo]['left']      # è un dizionario che rappresenta l'albero
    right = tree[nodo]['right']    # accediamo ai figli sinistro e destro
    if left is None and right is None:
        return 1                   # è una foglia
    return conta_foglie(tree, left) + conta_foglie(tree, right)

# Esempio di utilizzo

nodo = 'A'
print("Il numero di foglie nell'albero a partire dal nodo", nodo, "è", conta_foglie(tree, nodo))  
# Output: Il numero di foglie nell'albero a partire dal nodo A è 2

# Spiegazione:
# 1. La funzione conta_foglie prende un albero rappresentato come dizionario e un nodo come input.
# 2. Se il nodo è None, restituisce 0 (caso base).
# 3. Altrimenti, ottiene i figli sinistro e destro del nodo.
# 4. Se entrambi i figli sono None, il nodo è una foglia e restituisce 1.
# 5. Altrimenti, calcola ricorsivamente il numero di foglie nei figli sinistro e destro.
# 6. Restituisce la somma delle foglie nei figli.

# Complessità temporale: O(n), dove n è il numero di nodi nell'albero.
# Complessità spaziale: O(h), dove h è l'altezza dell'albero a causa della profondità della ricorsione.

# Il numero di foglie in un albero è una misura importante della sua struttura.

# Questa funzione può essere utilizzata per analizzare strutture ad albero,
# come alberi binari di ricerca, alberi AVL, alberi rosso-neri, ecc.

# Può essere utile in vari algoritmi che richiedono la conoscenza del numero di
# foglie, come bilanciamento degli alberi, calcolo della profondità, ecc.

# Inoltre, può essere adattata per alberi non binari modificando la struttura dati dell'albero.
# per esempio ecco un albero non binario: ___________________________________


non_binary_tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

def conta_foglie_non_binario(tree, nodo):
    if nodo is None or nodo not in tree:
        return 0              # caso base: nodo nullo o non esistente
    if not tree[nodo]:        # se il nodo non ha figli
        return 1
    count = 0
    for child in tree[nodo]:
        count += conta_foglie_non_binario(tree, child)  # somma le foglie dei figli
        return count
    
# Esempio di utilizzo

nodo = 'A'
print("Il numero di foglie nell'albero non binario a partire dal nodo", nodo, "è", conta_foglie_non_binario(non_binary_tree, nodo))
# Output: Il numero di foglie nell'albero non binario a partire dal nodo A è 4

# Spiegazione:
# 1. La funzione conta_foglie_non_binario prende un albero non binario rappresentato come dizionario e un nodo come input.
# 2. Se il nodo è None o non esiste nell'albero, restituisce 0 (caso base).
# 3. Se il nodo non ha figli, restituisce 1 (è una foglia).
# 4. Altrimenti, itera sui figli del nodo e somma il numero di foglie di ciascun figlio.
# 5. Restituisce il conteggio totale delle foglie.

# Complessità temporale: O(n), dove n è il numero di nodi nell'albero.
# Complessità spaziale: O(h), dove h è l'altezza dell'albero a causa della profondità della ricorsione.

# Il numero di foglie in un albero non binario è una misura importante della sua struttura.
# Questa funzione può essere utilizzata per analizzare strutture ad albero non binarie,
# come alberi generali, alberi n-ari, ecc.  
# Può essere utile in vari algoritmi che richiedono la conoscenza del numero di
# foglie, come bilanciamento degli alberi, calcolo della profondità, ecc.   
