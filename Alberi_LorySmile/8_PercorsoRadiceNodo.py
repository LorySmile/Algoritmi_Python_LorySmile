# Calcolare il percorso dalla radice a un nodo (Ramo)

def path_to_root(tree, nodo):
    p = []
    while nodo is not None :
        p.append(nodo)
        nodo = tree[nodo]['parent']
    return p[::-1]



