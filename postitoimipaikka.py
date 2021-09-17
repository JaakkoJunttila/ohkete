import json
import lue_tiedosto

postinumerot = lue_tiedosto.hae_postinumerot()

postinumero = input('Kirjoita postinumero: ')

kaupunki = postinumerot.get(postinumero)

print(kaupunki)