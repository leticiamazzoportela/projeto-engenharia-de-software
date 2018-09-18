import csv
import json

lista = 'ListaMacrofitas.csv'
nomes = []

with open(lista, 'r') as arquivo:
    reader = csv.reader(arquivo)
    for linha in reader:
        conteudo = linha[0].split()
        nome = conteudo[0] + " " + conteudo[1]
        nomes.append(nome)

macrofitas = 'macrofitas.json'

with open(macrofitas, 'w') as arq:
    json.dump(nomes, arq, indent=2)
