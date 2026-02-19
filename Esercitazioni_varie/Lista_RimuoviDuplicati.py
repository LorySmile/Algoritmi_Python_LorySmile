# Rimuovi duplicati in lista
def rimuovi_duplicati(lista):
    vista = []
    for x in lista:
        if x not in vista :
            vista.append(x)
    return vista

lista_y = [5, 3, 2, 8, 3]
print(rimuovi_duplicati(lista_y))

# Opzione 1: dict.fromkeys mantiene l'ordine
list(dict.fromkeys([1, 2, 2, 3, 3, 3]))  # [1, 2, 3]

# Opzione 2: manuale
seen = []
for x in [1, 2, 2, 3, 3, 3]:
    if x not in seen:
        seen.append(x)