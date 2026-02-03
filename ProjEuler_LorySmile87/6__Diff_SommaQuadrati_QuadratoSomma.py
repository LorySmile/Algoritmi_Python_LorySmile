# Trova la differenza tra la somma dei quadrati e il quadrato della somma dei primi 100 numeri naturali.

somma_quadrati = sum(i * i for i in range(1, 101))
quadrato_somma = sum(range(1, 101)) ** 2
differenza = quadrato_somma - somma_quadrati
print(differenza)  # la differenza è 25164150