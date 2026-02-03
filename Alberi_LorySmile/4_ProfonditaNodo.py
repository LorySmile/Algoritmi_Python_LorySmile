# Calcolare la profondità di un nodo (risalendo ai parent) in un albero binario.

tree = {
    'A': {'parent': None},
    'B': {'parent': 'A'},
    'C': {'parent': 'B'},
    'D': {'parent': 'C'}
}

# Iterativo: ________________________________________________

def profondita(tree, nodo):
    d = 0
    while tree[nodo]['parent'] is not None:
        nodo = tree[nodo]['parent']
        d += 1
    return d

# Esempio di utilizzo
nodo = 'C'
print("Il nodo", nodo, "ha profondità", profondita(tree, nodo))  # Output: La profondità del nodo C è 2

# Spiegazione:
# 1. La funzione profondita prende un albero rappresentato come dizionario e un nodo come input.
# 2. Inizializza una variabile d a 0 per tenere traccia della profondità.
# 3. Utilizza un ciclo while per risalire ai parent del nodo finché non raggiunge la radice (parent None).
# 4. Ad ogni iterazione, aggiorna il nodo al suo parent e incrementa d di 1.
# 5. Restituisce la profondità d del nodo.

# Complessità temporale: O(h), dove h è l'altezza dell'albero nel caso peggiore.
# Complessità spaziale: O(1), poiché utilizza solo variabili scalari.

# La profondità di un nodo è definita come il numero di archi dal nodo alla radice dell'albero.
# Un nodo radice ha profondità 0.

# Ricorsivo: ________________________________________________

def profondita(tree, nodo):
    if tree[nodo]['parent'] is None:
        return 0  # caso base: radice
    return 1 + profondita(tree, tree[nodo]['parent'])

# Esempio di utilizzo
nodo = 'D'
print("La profondità del nodo", nodo, "è", profondita(tree, nodo))  # Output: La profondità del nodo D è 3

# Spiegazione:
# 1. La funzione profondita prende un albero rappresentato come dizionario e un nodo come input.
# 2. Se il parent del nodo è None, restituisce 0 (caso base).
# 3. Altrimenti, chiama ricorsivamente se stessa con il parent del nodo e aggiunge 1 al risultato.
# 4. Restituisce la profondità del nodo.

# Complessità temporale: O(h), dove h è l'altezza dell'albero nel caso peggiore.
# Complessità spaziale: O(h), dove h è l'altezza dell'albero a causa della profondità della ricorsione.

# La profondità di un nodo è definita come il numero di archi dal nodo alla radice dell'albero.
# Un nodo radice ha profondità 0.

# Questa funzione può essere utilizzata per analizzare strutture ad albero,
# come alberi binari di ricerca, alberi AVL, alberi rosso-neri, ecc.
# Può essere utile in vari algoritmi che richiedono la conoscenza della profondità
# dei nodi, come bilanciamento degli alberi, calcolo dell'altezza, ecc.

# Inoltre, può essere adattata per alberi binari modificando la struttura dati dell'albero.
# Ecco un albero binario come esempio: ___________________________________

binary_tree = {
    'A': {'left': 'B', 'right': 'C', 'parent': None},
    'B': {'left': 'D', 'right': None, 'parent': 'A'},
    'C': {'left': None, 'right': None, 'parent': 'A'},
    'D': {'left': None, 'right': None, 'parent': 'B'}
}

def profondita_binario(tree, nodo):
    if tree[nodo]['parent'] is None:
        return 0  # caso base: radice
    return 1 + profondita_binario(tree, tree[nodo]['parent'])

# Esempio di utilizzo
nodo = 'D'
print("Il nodo", nodo, "ha profondità", profondita_binario(binary_tree, nodo))  # Output: La profondità del nodo D è 2   

# Spiegazione:
# 1. La funzione profondita_binario prende un albero binario rappresentato come dizionario e un nodo come input.
# 2. Se il parent del nodo è None, restituisce 0 (caso base).
# 3. Altrimenti, chiama ricorsivamente se stessa con il parent del nodo e aggiunge 1 al risultato.
# 4. Restituisce la profondità del nodo.   

# Complessità temporale: O(h), dove h è l'altezza dell'albero nel caso peggiore.
# Complessità spaziale: O(h), dove h è l'altezza dell'albero a causa della profondità della ricorsione.


