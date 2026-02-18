# Calcolare il Massimo Comun Divisore (Greatest Common Divisor)

def mcd(a, b):
    while b :
        a, b = b, a % b
    return a

print(mcd(8, 32))

# Calcolare il minimo comune multiplo (least common multiple)

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

print(mcm(8, 5434))
print(mcm(8, 32))
print(mcm(5, 2387))
