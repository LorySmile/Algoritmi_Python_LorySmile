# Determinare il fattore primo più grande di 600851475143.

n = 600851475143
fattore = 2
while fattore * fattore <= n:
    if n % fattore == 0:
        n //= fattore
    else:
        fattore += 1
print(n)

# il fattore primo più grande è 6857