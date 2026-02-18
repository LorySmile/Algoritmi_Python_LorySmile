# Primi 20 numeri di Fibonacci
nu = 20
a, b = 0, 1
for _ in range(nu):
    print(a, end=" ")
    a, b = b, a + b
print("")

# Fibonacci in funzione
def fibonacci(n):
    if n <= 1 :
        return n
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)
print("")
fibonacci(5)