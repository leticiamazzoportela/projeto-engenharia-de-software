import csv
import json
import os
import io

DIRNAME = os.path.dirname(__file__)


def readInput():
    nomes = []

    with open(os.path.join(DIRNAME, 'ListaMacrofitas.csv'), 'r') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            nomes.append(linha[0])

    return nomes


def saveCSV(species):
    with io.open(os.path.join(DIRNAME, 'output.csv'), 'w', encoding="UTF-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([
            "nome",
            "status flora brasil",
            "nome flora brasil",
            "status plantlist",
            "plantlist",
            "flora brasil x plantlist"
        ])
        for specie in species:
            try:
                flora_plant = ""
                if (specie.__contains__("florabrasil") and specie.__contains__("plantlist") and specie["plantlist"] != specie["florabrasil"] and specie["plantlist"] != "" and specie["florabrasil"] != ""):
                    flora_plant = "diferente"
                writer.writerow([
                    specie["nome"],
                    specie["status_florabrasil"],
                    specie["florabrasil"] if specie.__contains__(
                        "florabrasil") else "",
                    specie["status_plantlist"],
                    specie["plantlist"] if specie.__contains__(
                        "plantlist") else "",
                    flora_plant
                ])
            except:
                print(specie)


if __name__ == "__main__":
    saveCSV([
        {
            "nome": "teste",
            "status_florabrasil": "status_florabrasil",
            "florabrasil": "florabrasil",
            "status_plantlist": "status_plantlist",
            "plantlist": "plantlist"
        }
    ])
