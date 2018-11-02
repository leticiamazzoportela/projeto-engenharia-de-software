# encoding: utf-8

import requests
import json
import util
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_data(species):
    data = []
    driver = get_driver()
    for specie in species:
        print(specie)
        specie_name = specie.split(" ")
        name = specie_name[0] + " " + specie_name[1]
        r = requests.get(
            'http://servicos.jbrj.gov.br/flora/url/' + util.normalize(name))
        dado = json.loads(r.content)
        if(r.status_code == 200):
            if (dado.get('result')):
                url = dado.get('result')[0]['references']
                driver.get(url)
                # time.sleep(5)
                specie_data = craw_specie(driver)
                specie_data["name"] = specie
                data.append(specie_data)
    driver.close()
    return data


def get_driver():
    # don't load images
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference(
        'dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    # init the browser
    driver = webdriver.Firefox(firefox_profile=firefox_profile)
    return driver


def craw_specie(driver):
    specie = {}
    while(True):
        try:
            page = driver.page_source
            soup = BeautifulSoup(page, "lxml")
            grupo = soup.select(".grupo")
            specie['hierarchy'] = grupo[1].text
        except:
            time.sleep(0.3)
            continue
        break
    taxon = soup.select_one("#idFieldHierarquia").find_all('span')[4]
    # print(taxon)
    specie['family'] = taxon.text
    forma_vida = soup.select(".formaVida")
    specie['forma_de_vida'] = forma_vida[2].text.strip()
    substrato = soup.select(".substrato")
    specie['substrato'] = substrato[2].text.strip()
    origem = soup.select(".origem")
    specie['origem'] = origem[1].text.strip()
    endemismo = soup.select(".endemismo")
    specie['endemismo'] = endemismo[1].text.strip()
    confirmadas = []
    tablemap = soup.select_one(".distribGeoCerteza").find(
        "div", class_="tabelamapa")
    for div in tablemap.find_all("div", id=re.compile("idFieldCerteza.+")):
        words = re.sub(r"(^.*\(|\).*)", "", div.text)
        if (words != div.text):
            confirmadas += words.split(", ")
    duvidas = []
    for div in tablemap.find_all("div", id=re.compile("idFieldDuvida.+")):
        words = re.sub(r"(^.*\(|\).*)", "", div.text)
        if (words != div.text):
            duvidas += words.split(", ")

    specie["confirmadas"] = confirmadas
    specie["duvidas"] = duvidas
    return specie


if __name__ == "__main__":
    import json
    import util

    plantlist_data = json.loads(open("plant_flora.json").read())
    flora_list = util.get_list_flora_names(plantlist_data)

    data = get_data(flora_list)

    with open('src/data/floraData.json', 'w') as outfile:
        json.dump(data, outfile)
