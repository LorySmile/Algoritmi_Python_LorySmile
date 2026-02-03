# Trova il 10001-esimo numero primo.

# Funzione per verificare se un numero è primo
# Restituisce True se n è primo, altrimenti False

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Conta i numeri primi fino a trovare il 10001-esimo

count = 0
num = 1
while count < 10001:
    num += 1
    if is_prime(num):
        count += 1
print(num)  # il 10001-esimo numero primo è 104743