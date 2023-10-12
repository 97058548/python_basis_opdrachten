# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

vragen = ["Wat vind je van de huidige regering?", "Wat vind je van de Python-lessen tot nu toe?", "Wat vind jij de mooiste stad van Nederland?"]
antwoorden = []

for vraag in vragen:
    antwoord = input(vraag + " ")
    antwoorden.append(antwoord)

print("\nDank je wel voor je antwoorden!")
for i in range(len(vragen)):
    print(f"{vragen[i]} - Antwoord: {antwoorden[i]}")
