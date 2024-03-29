import csv
import json
import os
import xlsxwriter
import io
from util import normalize_str
from config import config

def readInput():
    nomes = []

    with open(config.filename, 'r') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            nomes.append(linha[0])

    return nomes


def saveSheet(species):
    # Create a workbook and add a worksheet.
    path = os.path.join(config.dirname, "plant_flora_valid_names.xlsx")
    workbook = xlsxwriter.Workbook(path)
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
        except Exception as e:
            print(e)

    workbook.close()


def save_info_sheet(flora_data, plant_data):
    # Create a workbook and add a worksheet.
    path = os.path.join(config.dirname, "info.xlsx")
    workbook = xlsxwriter.Workbook(path)

    save_flora_sheet(flora_data, workbook)
    save_plant_sheet(plant_data, workbook)

    workbook.close()


def save_flora_sheet(species, workbook):
    worksheet = workbook.add_worksheet("flora")

    col = 0
    row = 3

    title_format = workbook.add_format(properties={'font_color': 'red'})
    sub_title = workbook.add_format(properties={'bold': True})

    # put title on row 0
    worksheet.write(0, 0, "Flora do Brasil", title_format)
    worksheet.write(1, 0, "Nome das espécies - Status Flora = ACEITO", sub_title)
    worksheet.write(1, 1, "Hierarquia Taxonômica", sub_title)
    worksheet.write(1, 3, "Forma de Vida e Substrato", sub_title)
    worksheet.write(1, 5, "Origem", sub_title)
    worksheet.write(1, 6, "Endemismo", sub_title)
    worksheet.write(1, 7, "Distribuição", sub_title)
    worksheet.write(2, 1, "Grupo taxonômico")
    worksheet.write(2, 2, "Família")
    worksheet.write(2, 3, "Forma de Vida")
    worksheet.write(2, 4, "Substrato")
    worksheet.write(2, 7, "Ocorrências confirmadas")
    worksheet.write(2, 8, "Possíveis ocorrências")

    for specie in species:
        worksheet.write(row, 0, specie["name"])
        worksheet.write(row, 1, specie["hierarchy"])
        worksheet.write(row, 2, specie["family"])
        worksheet.write(row, 3, specie["forma_de_vida"])
        worksheet.write(row, 4, specie["substrato"])
        worksheet.write(row, 5, specie["origem"])
        worksheet.write(row, 6, specie["endemismo"])
        worksheet.write(row, 7, ", ".join(specie["confirmadas"]))
        worksheet.write(row, 8, ", ".join(specie["duvidas"]))
        
        row += 1

    # workbook.close()

def save_plant_sheet(species, workbook):
    worksheet = workbook.add_worksheet("plant")

    col = 0
    row = 3

    title_format = workbook.add_format(properties={'font_color': 'red'})
    sub_title = workbook.add_format(properties={'bold': True})

    # put title on row 0
    worksheet.write(0, 0, "Plantlist", title_format)
    worksheet.write(1, 0, "Nome das espécies - Status Plant = ACEITO", sub_title)
    worksheet.write(1, 1, "Hierarquia Taxonômica", sub_title)
    worksheet.write(1, 3, "Forma de Vida e Substrato", sub_title)
    worksheet.write(1, 5, "Origem", sub_title)
    worksheet.write(1, 6, "Endemismo", sub_title)
    worksheet.write(1, 7, "Distribuição", sub_title)
    worksheet.write(2, 1, "Grupo taxonômico")
    worksheet.write(2, 2, "Família")
    worksheet.write(2, 3, "Forma de Vida")
    worksheet.write(2, 4, "Substrato")
    worksheet.write(2, 7, "Ocorrências confirmadas")
    worksheet.write(2, 8, "Possíveis ocorrências")

    for specie in species:
        worksheet.write(row, 0, specie["name"])
        worksheet.write(row, 1, specie["hierarchy"])
        worksheet.write(row, 2, specie["family"])

        
        row += 1

    # workbook.close()

def save_notfound(notfound):
    path = os.path.join(config.dirname, "notfound.xlsx")
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()

    for i in range(len(notfound)):
        worksheet.write(i, 0, notfound[i])
    
    workbook.close()

def save_sinonimos(flora_data, plant_data):
    path = os.path.join(config.dirname, "info.xlsx")
    workbook = xlsxwriter.Workbook(path)

    save_flora_sinonimos(flora_data, workbook)
    save_plant_sinonimos(plant_data, workbook)

    workbook.close()

def save_occurrences(occurrences):
    path = os.path.join(config.dirname, "ocorrencias.xlsx")
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()

    title_format = workbook.add_format(properties={'font_color': 'red'})

    worksheet.write(0, 0, "planta", title_format)
    worksheet.write(0, 1, "Família", title_format)
    worksheet.write(0, 2, "Filo", title_format)
    worksheet.write(0, 3, "Ordem", title_format)
    worksheet.write(0, 4, "Genero", title_format)
    worksheet.write(0, 5, "especie", title_format)
    worksheet.write(0, 6, "Classe", title_format)
    worksheet.write(0, 7, "Coletor", title_format)
    worksheet.write(0, 8, "Pais", title_format)
    worksheet.write(0, 9, "Latitude", title_format)
    worksheet.write(0, 10, "Longitude", title_format)

    row = 1
    for plant in occurrences:
        for occurrence in occurrences[plant]:
            worksheet.write(row, 0, plant)
            worksheet.write(row, 1, occurrence["familia"])
            worksheet.write(row, 2, occurrence["filo"])
            worksheet.write(row, 3, occurrence["ordem"])
            worksheet.write(row, 4, occurrence["genero"])
            worksheet.write(row, 5, occurrence["especie"])
            worksheet.write(row, 6, occurrence["classe"])
            worksheet.write(row, 7, occurrence["coletor"])
            worksheet.write(row, 8, occurrence["pais"])
            worksheet.write(row, 9, occurrence["lat"])
            worksheet.write(row, 10, occurrence["long"])
            row += 1
    workbook.close()


if __name__ == "__main__":
    # saveSheet([
    #     {
    #         "nome": "Hygrophila guianensis Nees",
    #         "status_florabrasil": "Hygrophila costata Nees",
    #         "florabrasil": "flora brasil",
    #         "status_plantlist": "",
    #         "plantlist": "plant list"
    #     }
    # ])
    data = json.loads(open("data/occurrences.json").read())
    config.dirname = "/home/igornfaustino/Documents/code/faculdade/6_periodo/eng2"
    save_occurrences(data)
    # print(readInput())
