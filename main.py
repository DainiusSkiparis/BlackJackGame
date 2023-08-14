import random

from kortos import kalade, zaidejokortos, dyleriokortos

dylerio_suma = 0
zaidejo_suma = 0

dylerio_kortos = []
zaidejo_kortos = []

for _ in range(2):
    # korta = kalade.trauktikorta()
    dylerio_korta = random.choice(kalade.kalade)
    zaidejo_korta = random.choice(kalade.kalade)
    dylerio_suma += dylerio_korta.reiksmes_verte[dylerio_korta.reiksme]
    zaidejo_suma += zaidejo_korta.reiksmes_verte[zaidejo_korta.reiksme]
    dylerio_kortos.append(dylerio_korta)
    zaidejo_kortos.append(zaidejo_korta)

dyleriokortos(dylerio_kortos)
zaidejokortos(zaidejo_kortos)

print(f"Tavo suma: {zaidejo_suma}\n")

while True:
    print("+--------------------+")
    print("| 1 - Imti kortą     |")
    print("| 2 - Neimti kortos  |")
    print("| 0 - Baigti žaidimą |")
    print("+--------------------+")

    pasirinkimas = input("Pasirinkite veiksmą: ")

    if pasirinkimas == "1":
        korta = random.choice(kalade.kalade)
        # korta = kalade.trauktikorta()
        zaidejo_suma += korta.reiksmes_verte[korta.reiksme]
        zaidejo_kortos.append(korta)
        zaidejokortos(zaidejo_kortos)
        # print(f"Nauja korta: {korta.reiksme}{korta.simbolis}")
        print(f"Tavo nauja suma: {zaidejo_suma}\n")

    elif pasirinkimas == "2":
        print("Pasirinkote neimti kortos.")
        print(f"Tavo dabartinė suma: {zaidejo_suma}")

    elif pasirinkimas == "0":
        break

    else:
        print("Neteisingas pasirinkimas!")

print("Žaidimo pabaiga")

print("Dylerio kortos:")
for korta in dylerio_kortos:
    dylerio_suma += korta.reiksmes_verte[korta.reiksme]
    print(f"{korta.reiksme}{korta.simbolis}")

print(f"Dylerio suma: {dylerio_suma}\n")

print("Tavo kortos:")
for korta in zaidejo_kortos:
    print(f"{korta.reiksme}{korta.simbolis}")

print(f"Tavo suma: {zaidejo_suma}\n")
