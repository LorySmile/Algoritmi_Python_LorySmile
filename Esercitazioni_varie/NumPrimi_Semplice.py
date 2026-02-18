# Numeri Primi
def numeri_primi(n):
    if n < 2 :
        return False
    for i in range(2, int(n**0.5) + 1 ):
        if n % i == 0 :
            return False
    return True

# Trovo i numeri primi sotto 20
for num in range(20):
    if numeri_primi(num):
        print(num, end=" ")