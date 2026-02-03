# Trovare il numero di potenze distinte di a^b per 2 <= a <= 100 e 2 <= b <= 100.

potenze_distinte = set()

for a in range(2, 101):
    for b in range(2, 101):
        potenze_distinte.add(a ** b)
print(len(potenze_distinte))  # Il numero di potenze distinte è 9183