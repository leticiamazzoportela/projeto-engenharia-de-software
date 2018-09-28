import csv
import json
import os

DIRNAME = os.path.dirname(__file__)


def readInput():
    nomes = []

    with open(os.path.join(DIRNAME, 'ListaMacrofitas.csv'), 'r') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            conteudo = linha[0].split()
            nome = conteudo[0] + " " + conteudo[1]
            nomes.append(nome)

    with open(os.path.join(DIRNAME, 'data/macrofitas.json'), 'w') as arq:
        json.dump(nomes, arq, indent=2)


if __name__ == "__main__":
    readInput()
