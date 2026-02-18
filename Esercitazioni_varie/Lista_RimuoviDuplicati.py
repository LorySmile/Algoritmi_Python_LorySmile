# Rimuovi duplicati in lista
def rimuovi_duplicati(lista):
    vista = []
    for x in lista:
        if x not in vista :
            vista.append(x)
    return vista

lista_y = [5, 3, 2, 8, 3]
print(rimuovi_duplicati(lista_y))