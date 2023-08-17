from kortos import *
from pasirinkimai import pasirinkimas
from skaiciavimai import taskuskaiciavimas, tuzuskaiciavimas

tasku_suma = 0
tuzu_kiekis = 0

for _ in range(2):  # Padalinam po 2 kortas
    dylerio_korta = random.choice(kalade.kalade)
    zaidejo_korta = random.choice(kalade.kalade)

    dylerio_kortos.append(dylerio_korta)
    zaidejo_kortos.append(zaidejo_korta)

dyleriokortos(dylerio_kortos)
dylerio_tuzai = tuzuskaiciavimas(dylerio_kortos, tuzu_kiekis)
print(f"Tuzu: {dylerio_tuzai}")

dylerio_tasku_suma = taskuskaiciavimas(dylerio_kortos, tasku_suma, dylerio_tuzai)
print(f"Tasku suma: {dylerio_tasku_suma}")

zaidejokortos(zaidejo_kortos)
zaidejo_tuzai = tuzuskaiciavimas(zaidejo_kortos, tuzu_kiekis)
print(f"Tuzu: {zaidejo_tuzai}")

zaidejo_tasku_suma = taskuskaiciavimas(zaidejo_kortos, tasku_suma, zaidejo_tuzai)
print(f"Tasku suma: {zaidejo_tasku_suma}")

pasirinkimas(zaidejo_tasku_suma, zaidejo_kortos)
