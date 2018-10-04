# encoding: utf-8

import requests
import json
import os
import io
import util

DIRNAME = os.path.dirname(__file__)


def getNames():
    lista_nomes = []

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
            if(dado.get('result') == None): #checa se há resultado para essa espécie no Flora Brasil
                nomes['status'] = 'nao_encontrado'
                nomes['nome'] = specie
            else:
                nomes['status'] = ""
                nomes['nome'] = specie
                if(dado.get('result')[0]['taxonomicstatus'] == 'NOME_ACEITO'): #checa se o nome buscado é o aceito
                    nomes['status'] = 'nome_aceito'
                else:
                    nomes['status'] = 'sinonimo'
                    accepted_name = dado.get(
                        'result')[0]['acceptednameusage']
                    if (accepted_name):
                        nomes['nome_aceito'] = accepted_name
                    else:
                        nomes['status'] = 'nao_encontrado'
                        nomes['nome'] = specie
        else:
            nomes['status'] = 'nao_encontrado'
            nomes['nome'] = specie

        lista_nomes.append(nomes)
        
    # print(lista_nomes)

    with io.open(os.path.join(DIRNAME, 'data/data.json'), 'w', encoding='utf8') as arq:
        json.dump(lista_nomes, arq, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    getNames()
