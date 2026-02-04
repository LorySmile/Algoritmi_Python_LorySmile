# Ricerca in BST ______________________________________________________________________

""" 
Un BST (Binary Search Tree) ha questa regola:

        Nodo sinistro ≤ nodo corrente

        Nodo destro > nodo corrente

Per cercare un valore, basta confrontarlo con il nodo corrente e decidere se andare a sinistra o a destra. 

"""

class NodoBST:
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None

# Funzione per cercare un valore nel BST
def cerca_bst(nodo, chiave):
    if nodo is None:
        return False
    if chiave == nodo.valore:
        return True
    elif chiave < nodo.valore:
        return cerca_bst(nodo.sinistro, chiave)
    else:
        return cerca_bst(nodo.destro, chiave)
    
"""
Caso migliore: la chiave è alla radice → O(1)

Caso medio: si attraversa metà dell’albero bilanciato → O(log n)

Caso peggiore: albero degenerato (tipo lista) → O(n)

Nota: n = numero di nodi dell’albero.

"""

# Esempio di BST
radice = NodoBST(50)
radice.sinistro = NodoBST(30)
radice.destro = NodoBST(70)
radice.sinistro.sinistro = NodoBST(20)
radice.sinistro.destro = NodoBST(40)
radice.destro.sinistro = NodoBST(60)
radice.destro.destro = NodoBST(80)

# Test ricerca
print(cerca_bst(radice, 60))  # True
print(cerca_bst(radice, 25))  # False

# Inserimento in BST ____________________________________________________________________

"""
Per inserire un nuovo nodo, si segue la stessa logica della ricerca:

        Se il valore è minore → vai a sinistra

        Se il valore è maggiore → vai a destra

"""

def inserisci_bst(nodo, chiave):
    if nodo is None:
        return NodoBST(chiave)
    if chiave < nodo.valore:
        nodo.sinistro = inserisci_bst(nodo.sinistro, chiave)
    else:
        nodo.destro = inserisci_bst(nodo.destro, chiave)
    return nodo

"""
La logica è simile alla ricerca, perché dobbiamo trovare la posizione giusta.

Caso migliore: inserimento alla radice → O(1)

Caso medio: albero bilanciato → O(log n)

Caso peggiore: albero degenerato → O(n)

"""

# Inseriamo un nuovo nodo
radice = inserisci_bst(radice, 65)

# Visualizzo risultato dell'inserimento
# Visualizziamo con in-order
def in_order(nodo):
    if nodo:
        in_order(nodo.sinistro)
        print(nodo.valore, end=' ')
        in_order(nodo.destro)

print("Albero dopo inserimento (in-order):")
in_order(radice)



