# Più grande palindromo ottenuto dal prodotto di due numeri di tre cifre

def is_pal(n: int) -> bool:
    s = str(n)
    return s == s[::-1]
p4 = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        prod = i * j
        if is_pal(prod) and prod > p4:
            p4 = prod
print(p4)   # il più grande palindromo è 906609