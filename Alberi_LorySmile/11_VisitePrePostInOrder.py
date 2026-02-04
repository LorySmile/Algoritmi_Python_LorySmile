# Visite Pre-Order, Post-Order ed InOrder su un Albero

# Struttura di Albero semplice usando le classi:

class Nodo:
    def __init__(self, valore):      # Definisce il costruttore della classe, cioè il metodo che viene eseguito automaticamente quando fai Nodo('A'). # valore è il dato contenuto nel nodo (può essere una lettera, un numero, una stringa, ecc.)          
        self.valore = valore         # Salva il valore passato in input dentro l’oggetto. # self indica “questo nodo specifico”
        self.sinistro = None         # Crea il “puntatore” (riferimento) al figlio sinistro del nodo. # None significa: “per ora non c’è nessun figlio sinistro”.
        self.destro = None           # Crea il riferimento al figlio destro del nodo. # Anche qui None significa: “per ora non c’è nessun figlio destro”.

# Creiamo un albero di esempio
"""
        A
       / \
      B   C
     / \   \
    D   E   F
"""
radice = Nodo('A')
radice.sinistro = Nodo('B')
radice.destro = Nodo('C')
radice.sinistro.sinistro = Nodo('D')
radice.sinistro.destro = Nodo('E')
radice.destro.destro = Nodo('F')

# In-Order - Sinistro -> Nodo -> Destro

def in_order(nodo):
    if nodo:
        in_order(nodo.sinistro)
        print(nodo.valore, end=' ')
        in_order(nodo.destro)

print("Visita in-order:")
in_order(radice)           # Output: D B E A C F


# Pre-Order - Nodo -> Sinistro -> Destro

def pre_order(nodo):
    if nodo:
        print(nodo.valore, end=' ')
        pre_order(nodo.sinistro)
        pre_order(nodo.destro)

print("\nVisita pre-order:")
pre_order(radice)            # Output: A B D E C F


# Post-Order - Sinistro -> Destro -> Nodo

def post_order(nodo):
    if nodo:
        post_order(nodo.sinistro)
        post_order(nodo.destro)
        print(nodo.valore, end=' ')

print("\nVisita post-order:")
post_order(radice)               # D E B F C A

# Complessità computazionale O(n) e spaziale O(h).
# Caso peggiore O(n) - albero degenerato
# Caso migliore O(log n) - albero bilanciato
# Se si memorizzano i risultati in una lista: spazio aggiuntivo O(n)


