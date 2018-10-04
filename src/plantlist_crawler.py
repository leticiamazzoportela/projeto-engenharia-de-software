from bs4 import BeautifulSoup
import requests
import json
import os
import io
import util

DIRNAME = os.path.dirname(__file__)
BASE_URL = "http://www.theplantlist.org/"


def scrap_results(section_html, specie):
    # get the accepted item
    item = section_html.find("td", class_="Accepted")
    if(not item):
        # get a synonym
        item = section_html.find("td", class_="Synonym")
    if item:
        # go to the plant page
        link = item.select_one("a")
        page = requests.get(BASE_URL + link['href'])
        soup = BeautifulSoup(page.text, "lxml")
        section = soup.find("section")
        scrap_synonym(section, specie)


def scrap_synonym(section_html, specie):
    title = section_html.find("h1")
    subtitle = title.select_one(".subtitle")
    firstLink = subtitle.find("a")
    if(firstLink.text == "accepted"):
            specie["status"] = "nome_aceito"
    else:
        accepted_name = subtitle.find("span", class_="name")
        if(accepted_name):
            specie["status"] = "sinonimo"
            specie["nome_aceito"] = accepted_name.text


def scrap_info(source_html, specie):
    soup = BeautifulSoup(source_html, "lxml")
    section = soup.find("section")

    # Test if has more than one plant with the name
    header2 = section.find("h2")
    if(header2 and header2.text == "Results"):
        return scrap_results(section, specie)
    return scrap_synonym(section, specie)


def crawl_all_species(species):
    for specie in species:
        # print(specie["status"])
        if(specie["status"] == "nao_encontrado"):
            print(specie["nome"])
            page = requests.get(
                BASE_URL + "tpl1.1/search?q=" + util.normalize(specie["nome"]))
            scrap_info(page.text, specie)


def getNames():
    with open(os.path.join(DIRNAME, 'data/data.json')) as f:
        species = json.load(f)

    crawl_all_species(species)

    with io.open(os.path.join(DIRNAME, 'data/data.json'), 'w', encoding="UTF-8") as list_file:
        json.dump(species, list_file, indent=2, ensure_ascii=False)



if __name__ == "__main__":
    getNames()
