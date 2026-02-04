# Eliminare un nodo foglia dall'albero.

# Un nodo foglia è un nodo senza figli. 

class NodoBST:
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None

# Inserimento
def inserisci_bst(nodo, chiave):
    if nodo is None:
        return NodoBST(chiave)
    if chiave < nodo.valore:
        nodo.sinistro = inserisci_bst(nodo.sinistro, chiave)
    else:
        nodo.destro = inserisci_bst(nodo.destro, chiave)
    return nodo

# Per eliminarlo, basta trovare il nodo e settare il riferimento del genitore a None. ______________________________

def elimina_foglia(nodo, chiave):
    if nodo is None:
        return None
    if chiave < nodo.valore:
        nodo.sinistro = elimina_foglia(nodo.sinistro, chiave)
    elif chiave > nodo.valore:
        nodo.destro = elimina_foglia(nodo.destro, chiave)
    else:
        # Se è una foglia
        if nodo.sinistro is None and nodo.destro is None:
            return None
    return nodo

# Stampa dell'albero ___________________________________________________________

# Visite dell'albero
def in_order(nodo):
    if nodo:
        in_order(nodo.sinistro)
        print(nodo.valore, end=' ')
        in_order(nodo.destro)

def pre_order(nodo):
    if nodo:
        print(nodo.valore, end=' ')
        pre_order(nodo.sinistro)
        pre_order(nodo.destro)

def post_order(nodo):
    if nodo:
        post_order(nodo.sinistro)
        post_order(nodo.destro)
        print(nodo.valore, end=' ')

# Creazione albero
radice = NodoBST(50)
for val in [30, 70, 20, 40, 60, 80]:
    radice = inserisci_bst(radice, val)

# Visita prima dell'eliminazione
print("In-order prima:", end=' ')
in_order(radice)
print("\nPre-order prima:", end=' ')
pre_order(radice)
print("\nPost-order prima:", end=' ')
post_order(radice)

# Eliminazione nodi foglia 20 e 80
radice = elimina_foglia(radice, 20)
radice = elimina_foglia(radice, 80)

# Visita dopo l'eliminazione
print("\n\nIn-order dopo:", end=' ')
in_order(radice)
print("\nPre-order dopo:", end=' ')
pre_order(radice)
print("\nPost-order dopo:", end=' ')
post_order(radice)