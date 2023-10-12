# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

tekst = input("Geef de tekst die je wilt encrypten: ")
versleutelde_tekst = ""

verschuiving = 1  # Aantal posities om de letters te verschuiven

for karakter in tekst:
    if karakter.isalpha():
        is_kleine_letter = karakter.islower()
        basis = ord('a') if is_kleine_letter else ord('A')
        verschoven_code = ord(karakter) + verschuiving - basis
        verschoven_code = verschoven_code % 26  # Zorg ervoor dat we binnen het alfabet blijven
        verschoven_code += basis
        versleutelde_tekst += chr(verschoven_code)
    else:
        versleutelde_tekst += karakter

print("Versleutelde tekst:")
print(versleutelde_tekst)
