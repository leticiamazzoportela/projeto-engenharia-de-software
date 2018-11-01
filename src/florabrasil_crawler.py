# encoding: utf-8

import requests
import json
import util
from bs4 import BeautifulSoup


def get_data(species):
    for specie in species:
        specie_name = specie.split(" ")
        name = specie_name[0] + " " + specie_name[1]
        r = requests.get(
            'http://servicos.jbrj.gov.br/flora/url/' + util.normalize(name))
        dado = json.loads(r.content)
        if(r.status_code == 200):
            if (dado.get('result')):
                url = dado.get('result')[0]['references']
                print(url)


def craw_specie(url):
    page = requests.get(url)
    



get_data(["Echinodorus bolivianus (Rusby) Hom-Niels",
          "Echinodorus cordifolius (L.) Griseb. ",
          "Echinodorus floribundus (Seub.) Seub.",
          "Echinodorus glandulosus Rataj",
          "Echinodorus grandiflorus (Cham. & Schltdl.) Micheli",
          "Echinodorus grisebachii Small",
          "Echinodorus lanceolatus Rataj", ])
