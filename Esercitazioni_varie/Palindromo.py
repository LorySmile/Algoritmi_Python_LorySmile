# Palindromo
parola = "radar"
è_palindromo = True
for i in range(len(parola) // 2):
    if parola[i] != parola[-(i+1)]:
        è_palindromo = False
        break
print(è_palindromo)      # l'output è True perchè radar è palindromo
# else:                       altrimenti si può usare il FOR... ELSE: ...
#   è_palindromo = True

# Palindromo in definizione di Funzione
def palindromo(parola):
    return parola == parola[::-1]

print("-----")
print(palindromo("esse"))
print(palindromo("radar"))
print(palindromo("viavai"))

