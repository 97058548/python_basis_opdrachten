# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = ...

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

# Hier de rest van jouw code...

toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]
beschikbare_toppings = [topping[0] for topping in toppings]

while True:
    print("Maak een keuze uit onze toppings:", beschikbare_toppings)
    gekozen_topping = input()

    # Controleer of de gekozen topping in de lijst met beschikbare toppings zit
    if gekozen_topping in beschikbare_toppings:
        for topping, prijs in toppings:
            if gekozen_topping == topping:
                print(f"U heeft {gekozen_topping} besteld. Dat kost {prijs}")
                break
    else:
        print("Uw keuze zit niet in ons assortiment")

    nog_een_keer = input("Wil je nog een topping bestellen? (ja/nee): ")
    if nog_een_keer.lower() != "ja":
        break