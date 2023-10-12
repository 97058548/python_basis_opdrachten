# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...


gasten = ["Jesse", "Paul", "Kees", "Marie", "Hilda"]

print("Oorspronkelijke lijst van gasten:")
for gast in gasten:
    print(gast)

gast_die_niet_kan = input("Welke gast kan niet deelnemen? ")
if gast_die_niet_kan in gasten:
    gasten.remove(gast_die_niet_kan)

print("\nBijgewerkte lijst van gasten:")
for gast in gasten:
    print(gast)
    