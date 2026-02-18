# Primi 20 numeri di Fibonacci
nu = 20
a, b = 0, 1
for _ in range(nu):
    print(a, end=" ")
    a, b = b, a + b