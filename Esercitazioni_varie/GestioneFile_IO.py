# APRIRE FILE ---------------------------------------------------------------------
# Metodo base (DEVI chiudere il file!)
file = open("dati.txt", "r")  # "r" = read (lettura)
contenuto = file.read()
file.close()  # -----> NON dimenticare!

# Metodo MIGLIORE: with (chiude automaticamente!) <-----
with open("dati.txt", "r") as file:
    contenuto = file.read()
# Il file si chiude automaticamente qui.

"""

----- Modi di Apertura: -----

"r"   # Read (lettura) - default, errore se non esiste
"w"   # Write (scrittura) - crea nuovo o SOVRASCRIVE
"a"   # Append (aggiunge) - aggiunge alla fine
"r+"  # Read + Write
"rb"  # Read binary (file binari: immagini, pdf...)

"""

# LEGGERE FILE (metodi) --------------------------------------------------------------------
# read() - legge tutto il contenuto
with open("dati.txt", "r") as f:
    tutto = f.read()
    print(tutto)

# readline() - legge UNA riga alla volta
with open("dati.txt", "r") as f:
    riga1 = f.readline()
    riga2 = f.readline()

# readlines() - legge tutte le righe in una lista
with open("dati.txt", "r") as f:
    righe = f.readlines()         # ['riga1\n', 'riga2\n', ...]
    for riga in righe:
        print(riga.strip())       # .strip() rimuove \n

# Iterare direttamente (IL METODO MIGLIORE!)
with open("dati.txt", "r") as f:
    for riga in f:
        print(riga.strip())

# SCRIVERE FILE ------------------------------------------------------------------------------
# Scrivere (SOVRASCRIVE il file!)
with open("output.txt", "w") as f:
    f.write("Ciao mondo\n")
    f.write("Questa è la seconda riga\n")

# Aggiungere senza cancellare
with open("output.txt", "a") as f:
    f.write("Questa riga viene aggiunta\n")

# Scrivere lista di righe
righe = ["riga 1\n", "riga 2\n", "riga 3\n"]
with open("output.txt", "w") as f:
    f.writelines(righe)

# VERIFICARE SE ESISTE ---------------------------------------------------------------------------
import os
# Controllare se un file esiste
if os.path.exists("dati.txt"):
    print("Il file esiste")
else:
    print("File non trovato")
# Controllare se è un file o una directory
if os.path.isfile("dati.txt"):
    print("È un file")
if os.path.isdir("cartella"):
    print("È una directory")

# LAVORARE CON CSV --------------------------------------------------------------------------------
import csv

# Leggere CSV
with open("dati.csv", "r") as f:
    reader = csv.reader(f)
    for riga in reader:
        print(riga)                        # ogni riga è una lista

# Scrivere CSV
dati = [
    ["Nome", "Età", "Voto"],
    ["Lorenza", "21", "30"],
    ["Marco", "22", "28"]
]
with open("studenti.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(dati)

# CSV con dizionari (più comodo!)
with open("dati.csv", "r") as f:
    reader = csv.DictReader(f)
    for riga in reader:
        print(riga["Nome"], riga["Voto"])

# Esempio Pratico: conta parole in un file
def conta_parole(filename):
    try:
        with open(filename, "r") as f:
            testo = f.read()
            parole = testo.split()
            return len(parole)
    except FileNotFoundError:
        print("File non trovato!")
        return 0

print(conta_parole("articolo.txt"))

# GESTIONE ERRORI in un file ----------------------------------------------------------------------
try:
    with open("inesistente.txt", "r") as f:
        contenuto = f.read()
except FileNotFoundError:
    print("File non trovato!")
except PermissionError:
    print("Non hai i permessi!")
except Exception as e:
    print(f"Errore: {e}")

