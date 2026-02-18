# Funzione normale (return)
def numeri_return(n):
    result = []
    for i in range(n):
        result.append(i)
    return result         # restituisce TUTTA la lista

lista = numeri_return(5)  # [0, 1, 2, 3, 4] ← tutto in memoria

# Generatore (yield)
def numeri_yield(n):
    for i in range(n):
        yield i           # restituisce UN valore alla volta

gen = numeri_yield(5)     # <generator object>
for num in gen:
    print(num)            # 0, 1, 2, 3, 4 ← un valore alla volta