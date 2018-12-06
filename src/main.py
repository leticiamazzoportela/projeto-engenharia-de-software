import csv_util
import florabrasil_api
import plantlist_crawler
import specieslink_crawler
import plantlist_other_infos
import florabrasil_api
import gbif_api
import util
import json
from config import config
from tkinter import messagebox
import os
import triagem
import sys


def execute():
    config.l_acao["text"] = "processando lista de entrada....."
    csv_data = csv_util.readInput()

    # get names
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

    # save name
    csv_util.saveSheet(plantlist_data)

    # save not found
    csv_util.save_notfound(util.get_notfound_plants(plantlist_data))

    # Get infos
    plant_name = util.get_list_plantlist_name(plantlist_data)
    config.l_acao["text"] = "Buscando informações extras plantlists...."
    p_info_data = plantlist_other_infos.getNames(plant_name)

    flora_names = util.get_list_flora_names(plantlist_data)
    config.l_acao["text"] = "Buscando informações extras florabrasil...."
    f_info_data = florabrasil_api.getNames(flora_names)

    # save info
    csv_util.save_info_sheet(f_info_data, p_info_data)
    csv_util.save_sinonimos(f_info_data, p_info_data)

    valid_names = util.get_list_of_valid_names(plantlist_data)

    config.l_acao["text"] = "Buscando ocorrencias no gbif...."
    gbif = gbif_api.getOccurrences(valid_names)

    config.l_acao["text"] = "Buscando ocorrencias no species link...."
    specieslink = specieslink_crawler.get_data(valid_names)

    config.l_acao["text"] = "Validando ocorrencias...."
    config.l_plant["text"] = ""
    specieslink = triagem.read_spicieslink(specieslink)
    gbif = triagem.read_gbif(specieslink)

    occurrences = util.check_occurrences(specieslink, gbif)

    # save occurences
    config.l_acao["text"] = "salvando ocorrencias...."
    config.l_plant["text"] = ""
    csv_util.save_occurrences(occurrences)

    messagebox.showinfo("Sucesso", "Todas as informações já foram coletadas")
    config.l_acao["text"] = "Todas as ações finalizadas"
    config.l_plant["text"] = ""
    config.root.quit()
    
