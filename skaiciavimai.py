def taskuskaiciavimas(kortos, tasku_suma, tuzu_kiekis):
    for korta in kortos:
        tasku_suma += korta.reiksmes_verte[korta.reiksme]

    while tasku_suma > 21:
        if tuzu_kiekis > 0:
            tuzu_kiekis -= 1
            tasku_suma -= 10
        elif tuzu_kiekis == 0:
            print("GAME OVER!!!")
            break

    return tasku_suma


def tuzuskaiciavimas(kortos, tuzu_kiekis):
    for korta in kortos:
        if korta.reiksme == 'A':
            tuzu_kiekis += 1
    return tuzu_kiekis
