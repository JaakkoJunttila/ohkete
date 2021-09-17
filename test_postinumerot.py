import postinumerot
import lue_tiedosto

ERIKOISTAPAUKSET = {
    "43800": "KIVIJÄRVI",
    "91150": "YLI-OLHAVA",
    "65374": "SMART POST",
    "90210": "BEVERLY HILLS"
}

def test_nimella_vain_yksi_numero():
    numerot = postinumerot.get_paikan_numerot('Korvatunturi')

    assert len(numerot) == 1

def test_nimella_monta_numeroa():
    numerot = postinumerot.get_paikan_numerot('Helsinki')

    assert len(numerot) > 1

def test_postinumerot_omalla_datalla(mocker):
    oma_data = ERIKOISTAPAUKSET
    mocker.patch('lue_tiedosto.hae_postinumerot', return_value=oma_data)
    numerot = postinumerot.get_paikan_numerot('BEVERLY HILLS')

    assert postinumerot.tuloste(numerot) == 'Postinumerot: 90210'

def test_smartpost_yhdella_kirjoitusasulla():
    kirjasto = lue_tiedosto.hae_postinumerot()

    assert 'SMART POST' and 'SMART-POST' and 'SMARTPSOT' not in kirjasto.values()
