# Palindromo
parola = "radar"
è_palindromo = True
for i in range(len(parola) // 2):
    if parola[i] != parola[-(i+1)]:
        è_palindromo = False
#        break
#print(è_palindromo)
    else:
        print(è_palindromo)