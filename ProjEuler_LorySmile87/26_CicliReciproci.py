# Trovare il denominatore d < 1000 tale che 1/d abbia la rappresentazione decimale ciclica più lunga.

def ciclo_rec(d: int) -> int:
    resto_pos = {}
    resto = 1
    pos = 0
    while resto != 0:
        if resto in resto_pos:
            return pos - resto_pos[resto]  # lunghezza del ciclo
        resto_pos[resto] = pos
        resto = (resto * 10) % d
        pos += 1
    return 0  # se la divisione termina, non c'è ciclo

max_lunghezza = 0
denominatore = 0

for d in range(1, 1000):
    lunghezza = ciclo_rec(d)
    if lunghezza > max_lunghezza:
        max_lunghezza = lunghezza
        denominatore = d

print(denominatore)  # il denominatore con il ciclo più lungo è 983