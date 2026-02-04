# Calcolare il percorso dalla radice a un nodo (Ramo)

# Si parte dal nodo che ti interessa e si risale l’albero, seguendo i puntatori al padre.

def path_to_root(tree, nodo): 
    if nodo not in tree:
        return []       
    p = []                           # Lista che conterrà i nodi del percorso (il ramo).
    while nodo is not None :         # Continui finché non arrivi alla radice. La radice è riconoscibile perché il suo parent è None.
        p.append(nodo)               # Aggiungi il nodo corrente al percorso. Nota bene: stai andando dal basso verso l'alto.
        nodo = tree[nodo]['parent']  # Ti sposti al padre del nodo corrente. È il cuore dell'algoritmo: stai "scalando" l'albero.
    return p[::-1]                   # Siccome hai costruito il percorso dal nodo alla radice, la lista è al contrario.
                    # Con [::-1] la ribalti e ottieni: radice → ... → nodo

# Spiegazione:
# 1. Parto dal nodo di interesse.
# 2. Salgo tramite il campo 'parent' fino a quando nodo diventa None.
# 3. Durante la risalita, aggiungo ogni nodo ad una lista p.
# 4. Alla fine, p contiene il percorso dal nodo alla radice, 
#    quindi lo inverto con p[::-1] per ottenere l'ordine radice → ... → nodo

# Questo tipo di funzione è fondamentale quando serve calcolare:
# - LCA (Lowest Common Ancestor);
# - distanza tra nodi;
# - proprietà legate al cammino dalla radice.
# La Complessità è O(h) dove h è l'altezza dell'albero, 
# perchè al massimo si risale di un livello per nodo.

# Esempio di utilizzo con Albero Binario:

binary_tree = {
    'A': {'left': 'B', 'right': 'C', 'parent': None},
    'B': {'left': 'D', 'right': None, 'parent': 'A'},
    'C': {'left': None, 'right': None, 'parent': 'A'},
    'D': {'left': None, 'right': None, 'parent': 'B'}
}

percorso = path_to_root(binary_tree, 'D')            # Percorso dalla radice al nodo 'D'
print("Percorso radice → D:", percorso)             # Output atteso: ['A', 'B', 'D']

# Simbolo freccetta U+2192 
# Scrivi 2192 e premi Alt+X in Visual Studio Code per fare la freccetta, 
#                              oppure scrivi -> ... ;D

# Non funziona senza parent; 
# è il motivo per cui molte strutture dati reali (filesystem, AST, DOM) memorizzano il padre; 
# rende banali problemi che altrimenti richiedono DFS + memoria ausiliaria.