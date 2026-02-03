# Trovare l'indice del primo numero di Fibonacci che ha 1000 cifre.

a, b = 1, 1
index = 2

while len(str(a)) < 1000:  # continua finché il numero di cifre di 'a' è inferiore a 1000
    a, b = b, a + b
    index += 1

print(index)               # l'indice è 4782