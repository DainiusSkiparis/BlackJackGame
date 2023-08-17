import random

dylerio_kortos = []
zaidejo_kortos = []


class Korta:
    def __init__(self, simbolis, reiksme):
        self.simbolis = simbolis
        self.reiksme = reiksme
        self.reiksmes_verte = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
                               'Q': 10, 'K': 10, 'A': 11}


class KortuKalade:
    def __init__(self):
        self.simboliai = ['♠', '♥', '♦', '♣']
        self.reiksmes = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # self.simboliai = ['♠']
        # self.reiksmes = ['K', 'A']
        # self.kalade = [Korta(simbolis, reiksme) for simbolis in self.simboliai for reiksme in self.reiksmes]

        self.kaladziu_kiekis = 6  # Nurodome, kiek kaladžių norime sukurti
        self.kalade = [Korta(simbolis, reiksme) for simbolis in self.simboliai for reiksme in self.reiksmes for _ in
                       range(self.kaladziu_kiekis)]

        random.shuffle(self.kalade)


# Sukuriamas kortu kalades objektas
kalade = KortuKalade()


def zaidejokortos(kortos):
    print("\nTavo kortos:", end=' ')
    for korta in kortos:
        print(f"{korta.reiksme}{korta.simbolis}", end=' ')
    print()


def dyleriokortos(kortos):
    print("\nDylerio kortos:", end=' ')
    for korta in kortos:
        print(f"{korta.reiksme}{korta.simbolis}", end=' ')
    print()
