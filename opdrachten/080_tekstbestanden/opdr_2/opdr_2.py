# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
getal = random.randint(1,100)
raadGetal = 0
teller = 0
while raadGetal != getal: 
    raadGetal = input(str(teller +1) + ": Raad het getal: ")
    #check input for stop
    if(raadGetal.lower()=='stop'):
        exit()
    #check if input isdigit
    if not raadGetal.isdigit():
        print("Dit is geen getal.")
    else:
        #convert input to integer
        raadGetal = int(raadGetal)
        if raadGetal < 1 or raadGetal > 100:
            print("vul een getal tussen 1 en 100 in....")        
        elif getal < raadGetal:
            print("Onjuist, het getal is lager")
        elif getal > raadGetal:
            print("Onjuist, het getal is hoger")
        teller += 1
print("Dit is het juiste getal. Geraden in "+str(teller)+" beurten")