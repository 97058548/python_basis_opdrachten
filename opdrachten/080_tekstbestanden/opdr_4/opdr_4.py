# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:

# Party enquete

# Lijst met vragen
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Lijst om de feestgangers op te slaan
feestgangers = []

# Loop om de vragen te stellen
for vraag in vragen:
    antwoord = input(f"{vragen.index(vraag) + 1}. {vraag}\n")
    feestganger = {}
    feestganger['voornaam'] = antwoord if 'voornaam' not in feestganger else feestganger['voornaam']
    feestganger['achternaam'] = antwoord if 'achternaam' not in feestganger else feestganger['achternaam']
    feestganger['drank'] = antwoord if 'drank' not in feestganger else feestganger['drank']
    feestganger['eten'] = antwoord if 'eten' not in feestganger else feestganger['eten']
    feestgangers.append(feestganger)

# Schrijf de gegevens naar een tekstbestand
with open("feestgangers.txt", "w") as bestand:
    for feestganger in feestgangers:
        bestand.write("----\n")
        bestand.write(f"voornaam: {feestganger['voornaam']}\n")
        bestand.write(f"achternaam: {feestganger['achternaam']}\n")
        bestand.write(f"drank: {feestganger['drank']}\n")
        bestand.write(f"eten: {feestganger['eten']}\n")
        bestand.write("----\n")

print("\nBedankt voor het invullen!")
print("See you at the party.")
