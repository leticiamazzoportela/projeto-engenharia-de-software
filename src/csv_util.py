import csv
import json
import os
import xlsxwriter
import io
from util import normalize_str

DIRNAME = os.path.dirname(__file__)


def readInput():
    nomes = []

    with open(os.path.join(DIRNAME, 'ListaMacrofitas.csv'), 'r') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            nomes.append(linha[0])

    return nomes


def saveSheet(species):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('output.xlsx')
    worksheet = workbook.add_worksheet()

    col = 0
    row = 1

    title_format = workbook.add_format(properties={'font_color': 'red'})

    # put title on row 0
    worksheet.write(0, 0, "Nome Especie", title_format)
    worksheet.write(0, 1, "Status Flora", title_format)
    worksheet.write(0, 2, "Nome Flora", title_format)
    worksheet.write(0, 3, "Observacao", title_format)
    worksheet.write(0, 4, "Status Plantlist", title_format)
    worksheet.write(0, 5, "Nome Plantlist", title_format)
    worksheet.write(0, 6, "Observacao", title_format)
    worksheet.write(0, 7, "Flora x Plantlist", title_format)

    for specie in species:
        try:
            flora_plant = ""
            obs_flora = ""
            obs_plantlist = ""

            # check flora x plant
            if (specie.__contains__("florabrasil") and specie.__contains__("plantlist") and specie["florabrasil"] != "" and specie["plantlist"] != ""):
                name_plantlist = specie["plantlist"].split(
                    " ")[0] + " " + specie["plantlist"].split(" ")[1]
                name_florabrasil = specie["florabrasil"].split(
                    " ")[0] + " " + specie["florabrasil"].split(" ")[1]

                flora_plant = "diferente" if name_plantlist != name_florabrasil else ""

            if (specie.__contains__("florabrasil") and
                    specie["florabrasil"] != "" and
                    normalize_str(specie["florabrasil"]) != normalize_str(specie["nome"])):
                nome_tokens = specie["nome"].split(" ")
                flora_token = specie["florabrasil"].split(" ")

                if (normalize_str(nome_tokens[0]) != normalize_str(flora_token[0])):
                    obs_flora = "Genero Diferente"
                elif (normalize_str(nome_tokens[1]) != normalize_str(flora_token[1])):
                    obs_flora = "Especie Diferente"
                else:
                    obs_flora = "Autor Diferente"

            if (specie.__contains__("plantlist") and specie["plantlist"] != "" and specie["plantlist"] != specie["nome"]):
                nome_tokens = specie["nome"].split(" ")
                plantlist_token = specie["plantlist"].split(" ")

                if (nome_tokens[0] != plantlist_token[0]):
                    obs_plantlist = "Genero Diferente"
                elif (nome_tokens[1] != plantlist_token[1]):
                    obs_plantlist = "Especie Diferente"
                else:
                    obs_plantlist = "Autor Diferente"

            worksheet.write(row, 0, specie["nome"])
            worksheet.write(row, 1, specie["status_florabrasil"]
                            if specie["status_florabrasil"] != "nao_encontrado" else "")
            worksheet.write(row, 2, specie["florabrasil"] if specie.__contains__(
                "florabrasil") else "")
            worksheet.write(row, 3, obs_flora)
            worksheet.write(row, 4, specie["status_plantlist"]
                            if specie["status_plantlist"] != "nao_encontrado" else "")
            worksheet.write(row, 5, specie["plantlist"] if specie.__contains__(
                "plantlist") else "")
            worksheet.write(row, 6, obs_plantlist)
            worksheet.write(row, 7, flora_plant)
            row += 1
        except:
            print(specie)

    workbook.close()


if __name__ == "__main__":
    saveSheet([
        {
            "nome": "Hygrophila guianensis Nees",
            "status_florabrasil": "Hygrophila costata Nees",
            "florabrasil": "flora brasil",
            "status_plantlist": "",
            "plantlist": "plant list"
        }
    ])
