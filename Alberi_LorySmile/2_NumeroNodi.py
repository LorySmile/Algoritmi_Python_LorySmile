# Calcolare il numero di nodi in un albero binario.

tree = {
    'A': {'left': 'B', 'right': 'C'},
    'B': {'left': 'D', 'right': None},
    'C': {'left': None, 'right': None},
    'D': {'left': None, 'right': None}
}

def conta_nodi(tree, nodo):
    if nodo is None:
        return 0    # caso base: nodo nullo
    left = tree[nodo]['left']                   # è un dizionario che rappresenta l'albero
    right = tree[nodo]['right']                 # accediamo ai figli sinistro e destro
    return 1 + conta_nodi(tree, left) + conta_nodi(tree, right) 

# Esempio di utilizzo

nodo = 'A'
print("Il numero di nodi nell'albero a partire dal nodo", nodo, "è", conta_nodi(tree, nodo))  
# Output: Il numero di nodi nell'albero a partire dal nodo A è 4

# Spiegazione:
# 1. La funzione conta_nodi prende un albero rappresentato come dizionario e un nodo come input.
# 2. Se il nodo è None, restituisce 0 (caso base).
# 3. Altrimenti, ottiene i figli sinistro e destro del nodo.
# 4. Calcola ricorsivamente il numero di nodi nei figli sinistro e destro.
# 5. Restituisce 1 (per il nodo corrente) più la somma dei nodi nei figli.

# Complessità temporale: O(n), dove n è il numero di nodi nell'albero.
# Complessità spaziale: O(h), dove h è l'altezza dell'albero a causa della profondità della ricorsione.

# Il numero di nodi in un albero è una misura fondamentale della sua dimensione.
# Questa funzione può essere utilizzata per analizzare strutture ad albero,
# come alberi binari di ricerca, alberi AVL, alberi rosso-neri, ecc.
# Può essere utile in vari algoritmi che richiedono la conoscenza del numero di
# nodi, come bilanciamento degli alberi, calcolo della profondità, ecc.

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

def conta_nodi_non_binario(tree, nodo):
    if nodo is None or nodo not in tree:
        return 0              # caso base: nodo nullo o non esistente
    count = 1                 # conta il nodo corrente
    for child in tree[nodo]:                          # itera sui figli del nodo
        count += conta_nodi_non_binario(tree, child)  # somma i nodi dei figli
    return count

# Esempio di utilizzo
nodo = 'A'
print("Il numero di nodi nell'albero non binario a partire dal nodo", nodo, "è", conta_nodi_non_binario(non_binary_tree, nodo))
# Output: Il numero di nodi nell'albero non binario a partire dal nodo A è 7

# Spiegazione:
# 1. La funzione conta_nodi_non_binario prende un albero non binario rappresentato come dizionario e un nodo come input.
# 2. Se il nodo è None o non esiste nell'albero, restituisce 0 (caso base).
# 3. Inizializza un contatore a 1 per il nodo corrente.
# 4. Itera su tutti i figli del nodo, sommando ricorsivamente il numero di nodi di ciascun figlio.
# 5. Restituisce il conteggio totale dei nodi.

# Complessità temporale: O(n), dove n è il numero di nodi nell'albero.
# Complessità spaziale: O(h), dove h è l'altezza dell'albero a causa della profondità della ricorsione.
