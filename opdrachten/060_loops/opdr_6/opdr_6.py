# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

pizza_lijst = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabetische volgorde
pizza_lijst.sort(reverse=False)
print(pizza_lijst)

# Voeg een nieuwe pizza toe
pizza_lijst.append('yo-favorito')
print(pizza_lijst)
# Verwijder de minst favoriete pizza
pizza_lijst.remove('olivio')
print(pizza_lijst)
# Print de eerste 3 pizza's
print(pizza_lijst[:3])

# Print de middelste pizza (let op: dit is geen efficiënte methode)
print([pizza_lijst[len(pizza_lijst) // 2]])

# Print de laatste 3 pizza's
print(pizza_lijst[-3:])
