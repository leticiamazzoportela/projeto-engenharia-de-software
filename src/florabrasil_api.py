# encoding: utf-8

import requests
import json
import os
import io
import util

DIRNAME = os.path.dirname(__file__)


def getNames():
    lista_nomes = []
    nao_encontrados = []

    with open(os.path.join(DIRNAME, 'data/macrofitas.json')) as f:
        species = json.load(f)

    for specie in species:
        print(specie)
        nomes = {}

        specie_name = specie.split(" ")
        name = specie_name[0] + " " + specie_name[1]
        r = requests.get(
            'http://servicos.jbrj.gov.br/flora/taxon/' + util.normalize(name))
        dado = json.loads(r.content)
        if(r.status_code == 200):
            if(dado.get('result') == None):
                nao_encontrados.append(specie)
            else:
                nomes['nome_passado'] = specie
                if(dado.get('result')[0]['taxonomicstatus'] == 'NOME_ACEITO'):
                    nomes['nome_correto'] = dado.get(
                        'result')[0]['scientificname']
                else:
                    accepted_name = dado.get(
                        'result')[0]['acceptednameusage']
                    if (accepted_name):
                        nomes['nome_correto'] = accepted_name
                    else:
                        nao_encontrados.append(specie)
                lista_nomes.append(nomes.copy())
        else:
            print(r.status_code)

    macrofitas = 'nome_validado.json'

    with io.open(os.path.join(DIRNAME, 'data/florabrasil_data.json'), 'w', encoding='utf8') as arq:
        json.dump(lista_nomes, arq, indent=2, ensure_ascii=False)

    with io.open(os.path.join(DIRNAME, 'data/florabrasil_NOTFOUND.json'), 'w', encoding='utf8') as arq:
        json.dump(nao_encontrados, arq, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    getNames()
