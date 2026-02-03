# Calcolare la milionesima permutazione lessicografica della sequenza di cifre da 0 a 9.

from itertools import permutations
digits = "0123456789"
perms = list(permutations(digits))
millionth_perm = ''.join(perms[999999])  # 0-indexed, so 999999 is the millionth permutation

print(millionth_perm)  # la milionesima permutazione è 2783915460