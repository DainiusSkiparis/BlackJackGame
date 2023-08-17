def zaidejokortosvienodos(zaidejo_kortos):  # patikrinam ar vienodos kortu reiksmes
    for i in range(len(zaidejo_kortos)):
        for j in range(i + 1, len(zaidejo_kortos)):
            if zaidejo_kortos[i].reiksmes_verte[zaidejo_kortos[i].reiksme] == zaidejo_kortos[j].reiksmes_verte[zaidejo_kortos[j].reiksme]:
                return True  # Jei vienodos kortos
    return False  # Jei kortos skirtingos


def arblackjack():
    pass
