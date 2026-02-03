# Trovare il prodotto a*b*c della terzina pitagorica (a, b, c) 
#         tale che a + b + c = 1000 e a² + b² = c²

for a in range(1, 1000):
    for b in range(a + 1, 1000 - a):
        c = 1000 - a - b             
        if a * a + b * b == c * c: 
            prodotto = a * b * c
print(prodotto)                        # il prodotto è 31875000