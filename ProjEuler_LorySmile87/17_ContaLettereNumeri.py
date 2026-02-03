# Conta le lettere nei numeri da 1 a 1000 in forma letterale (in italiano)

def numero_in_lettere(n: int) -> str:
    unita = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove"]
    decine = ["", "dieci", "venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]
    speciali = {
        11: "undici", 12: "dodici", 13: "tredici", 14: "quattordici",
        15: "quindici", 16: "sedici", 17: "diciassette", 18: "diciotto", 19: "diciannove"
    }
    centinaia = ["", "cento", "duecento", "trecento", "quattrocento",
                 "cinquecento", "seicento", "settecento", "ottocento", "novecento"]

    if n == 1000:
        return "mille"
    
    lettere = ""
    c = n // 100
    d = (n % 100) // 10
    u = n % 10

    if c > 0:
        lettere += centinaia[c]
        if d == 8:  # Elisione della 'o' in 'cento' davanti a 'ottanta'
            lettere = lettere[:-1]

    if d == 1 and u > 0:
        lettere += speciali[10 + u]
    else:
        if d > 0:
            lettere += decine[d]
            if u == 1 or u == 8:  # Elisione della vocale finale in decine
                lettere = lettere[:-1]
        if u > 0:
            lettere += unita[u]

    return lettere 
total_letters = sum(len(numero_in_lettere(i)) for i in range(1, 1001))
print(total_letters)  # Il totale delle lettere è 21124
