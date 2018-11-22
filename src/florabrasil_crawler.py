# encoding: utf-8

import requests
import json
import util

FLORA_URL = "http://floradobrasil.jbrj.gov.br/reflora/listaBrasil/ConsultaPublicaUC/ResultadoDaConsultaCarregaTaxonGrupo.do?&idDadosListaBrasil="
FLORA_OFICIAL_API = "http://servicos.jbrj.gov.br/flora/taxon/"

def get_data(species):
    data = []
    for specie in species:
        print(specie)
        name = util.remove_author(specie)
        r = requests.get(
            FLORA_OFICIAL_API + util.normalize(name))
        dado = json.loads(r.content)
        if(r.status_code == 200):
            if (dado.get('result')):
                plant_id = dado.get('result')[0]['taxonid']
                specie_data = get_specie_data(plant_id)
                specie_data["family"] = dado.get('result')[0]['family']
                specie_data["hierarchy"] = dado.get('result')[0]['higherclassification'].split(";")[1]
                specie_data["name"] = specie
                data.append(specie_data)
    
    return data

def get_specie_data(id):
    r = requests.get(FLORA_URL + id)
    specie = {}
    if (r.content != b'erro'):
        content = json.loads(r.content)
        specie['origem'] = content["origem"]
        specie["forma_de_vida"] = content["formaVida"][0] if len(content["formaVida"]) > 0 else ""
        specie["endemismo"] = content["endemismo"]
        specie['substrato'] = content["substrato"][0] if len(content["substrato"]) > 0 else ""
        certeza = []
        duvidas = []
        for key in content.keys():
            if("distribuicaoGeograficaCerteza" in key):
                try:
                    certeza += str(content[key]).split("(")[1].split(")")[0].split(", ")
                except:
                    pass
            if("distribuicaoGeograficaDuvida" in key):
                try:
                    duvidas += str(content[key]).split("(")[1].split(")")[0].split(", ")
                except:
                    pass
        specie["confirmadas"] = certeza
        specie["duvidas"] = duvidas
    return specie
    


if __name__ == "__main__":
    import json
    import util

    data = json.loads(open("data/plant_flora.json").read())
    flora_list = util.get_list_flora_names(data)

    data = get_data(flora_list)

    with open('data/floraData.json', 'w') as outfile:
        json.dump(data, outfile)
