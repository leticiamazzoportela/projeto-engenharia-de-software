import csv_util
import florabrasil_api
import plantlist_crawler
import specieslink_crawler
import util
import json
from config import config
from tkinter import messagebox


def execute():
    config.l_acao["text"] = "processando lista de entrada....."
    csv_data = csv_util.readInput()

    try:
        # 	print("Verificando nomes.....")
        config.l_acao["text"] = "analisando flora do brasil...."
        florabrasil_data = florabrasil_api.getNames(csv_data)

        config.l_acao["text"] = "analisando plantlist...."
        plantlist_data = plantlist_crawler.getNames(florabrasil_data)
    except ConnectionError:
        messagebox.showerror(
            "falha na rede", "Falha na rede... porfavor tente novamente mais tarde...")
        exit(1)

    # with open('plant_flora.json', 'w') as outfile:
    #     json.dump(plantlist_data, outfile)

    # plantlist_data = json.loads(open("data/plant_flora.json").read())

    # # print("Salvando CSV")
    # # csv_util.saveSheet(plantlist_data)

    valid_names = util.get_list_of_valid_names(plantlist_data)

    config.l_acao["text"] = "Buscando ocorrencias no species link...."
    specieslink = specieslink_crawler.get_data(valid_names)

    # with open('data/specieslink.json', 'w') as outfile:
    #     json.dump(specieslink, outfile)
