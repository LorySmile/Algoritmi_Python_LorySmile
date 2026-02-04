# Operazioni su Matrici

matrice = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Somma
somma = sum(sum(riga) for riga in matrice)
print("Somma:", somma)  # 45

# Diagonale principale
diagonale = [matrice[i][i] for i in range(len(matrice))]
print("Diagonale:", diagonale)  # [1,5,9]

# Massimo elemento
massimo = max(max(riga) for riga in matrice)
print("Massimo:", massimo)  # 9

# Complessità:
#   Somma → O(m*n)
#   Diagonale → O(min(m,n))
#   Massimo → O(m*n)