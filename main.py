from kortos import kalade

# Traukiame ir atspausdiname dvi kortas
print("Traukiamos kortos:")
dylerio_korta1 = kalade.traukti_korta()
dylerio_korta2 = kalade.traukti_korta()
zaidejo_korta1 = kalade.traukti_korta()
zaidejo_korta2 = kalade.traukti_korta()
zaidejo_korta3 = kalade.traukti_korta()
zaidejo_korta4 = kalade.traukti_korta()

# if korta1 and korta2:
print(f"{dylerio_korta1.reiksme}{dylerio_korta1.simbol} {dylerio_korta2.reiksme}{dylerio_korta2.simbol}")
suma1 = dylerio_korta1.reiksmes_verte[dylerio_korta1.reiksme] + dylerio_korta2.reiksmes_verte[dylerio_korta2.reiksme]
print(f"Kortų suma: {suma1}")

print(f"{zaidejo_korta1.reiksme}{zaidejo_korta1.simbol} {zaidejo_korta2.reiksme}{zaidejo_korta2.simbol}")
suma2 = zaidejo_korta1.reiksmes_verte[zaidejo_korta1.reiksme] + zaidejo_korta2.reiksmes_verte[zaidejo_korta2.reiksme]
print(f"Kortų suma: {suma2}")

