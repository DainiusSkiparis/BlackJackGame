from tikrinimai import zaidejokortosvienodos


def pasirinkimuprintas():
    print("| 1 - Imti kortą          |")
    print("| 2 - Neimti kortos       |")
    print("| 3 - Dvigubinti statyma  |")

def pasirinkimas(zaidejo_tasku_suma, zaidejo_kortos):
    while zaidejo_tasku_suma <= 21:
        print("+-------------------------+")
        if zaidejokortosvienodos(zaidejo_kortos):
            pasirinkimuprintas()
            print("| 4 - Isskirti kortas     |")
            print("+-------------------------+")

            pasirinkimas = input("Pasirinkite veiksmą: ")
            print(f"pasirinkote: {pasirinkimas}")
            break
        else:
            pasirinkimuprintas()
            print("+-------------------------+")

            pasirinkimas = input("Pasirinkite veiksmą: ")
            print(f"pasirinkote: {pasirinkimas}")
            break
