import json
import lue_tiedosto

def main():
    syotetty_paikka = input('Kirjoita postitoimipaikka: ')
    saadut_numerot = get_paikan_numerot(syotetty_paikka)
    print(tuloste(saadut_numerot))

def get_paikan_numerot(postitoimipaikka):
    postinumerot = lue_tiedosto.hae_postinumerot()
    paikan_numerot = []

    for numero in postinumerot:
        if postinumerot.get(numero) == postitoimipaikka.upper():
            paikan_numerot += [numero]

    return paikan_numerot

def tuloste(numerot):
    if numerot:
        return 'Postinumerot: ' + ', '.join(numerot)
    else:
        return 'Postitoimipaikkaa ei löytynyt!'

if __name__ == '__main__':
    main()
