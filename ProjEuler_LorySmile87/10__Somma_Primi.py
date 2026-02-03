# Trova la somma dei numeri primi inferiori a 2 milioni.

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_sum = sum(i for i in range(2, 2000000) if is_prime(i))
print(prime_sum)

# Spiegazione: La funzione is_prime verifica se un numero è primo. 
# La somma viene calcolata iterando su tutti i numeri da 2 a 2 milioni 
# e sommando quelli che sono primi. Il risultato finale è la somma 
# di tutti i numeri primi inferiori a 2 milioni, che è 142913828922.