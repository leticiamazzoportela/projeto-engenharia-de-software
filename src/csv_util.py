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


def saveCSV():
    with io.open(os.path.join(DIRNAME, 'data/data.json'), 'r', encoding="UTF-8") as f:
        species = json.load(f)
    with io.open(os.path.join(DIRNAME, 'output.csv'), 'w', encoding="UTF-8") as csv_file:
        writer = csv.writer(csv_file)
    
        for specie in species:
            writer.writerow([specie["status"], specie["nome"], specie["nome_aceito"] if specie.__contains__("nome_aceito") else ""])


if __name__ == "__main__":
    saveCSV()
    print(readInput())
