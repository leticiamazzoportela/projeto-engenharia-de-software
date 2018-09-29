import csv
import json
import os
import io
from util import normalize

DIRNAME = os.path.dirname(__file__)


def readInput():
    nomes = []

    with open(os.path.join(DIRNAME, 'ListaMacrofitas.csv'), 'r') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            # conteudo = linha[0].split()
            # nome = conteudo[0] + " " + conteudo[1]
            nomes.append(linha[0])

    with io.open(os.path.join(DIRNAME, 'data/macrofitas.json'), 'w', encoding='UTF-8') as arq:
        json.dump(nomes, arq, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    readInput()
