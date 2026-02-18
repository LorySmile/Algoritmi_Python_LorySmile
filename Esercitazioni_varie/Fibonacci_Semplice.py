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
print("")

# Fibonacci con lista e append()
def fibonacci_lista(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

fib = fibonacci_lista(10)  
print(fib)                               # [0,1,1,2,3,5,8,13,21,34] ← tutto in RAM

# Fibonacci con yield (generatore)
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci_gen(10):
    print(num)                           # stampa uno alla volta, senza sprecare memoria