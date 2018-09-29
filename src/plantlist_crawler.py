from bs4 import BeautifulSoup
import requests
import json
import os
import io
import util

DIRNAME = os.path.dirname(__file__)
BASE_URL = "http://www.theplantlist.org/"


def scrap_results(section_html, specie, name_list, not_found):
    item = section_html.find("td", class_="Accepted")
    if(not item):
        item = section_html.find("td", class_="Synonym")
    if item:
        link = item.select_one("a")
        page = requests.get(BASE_URL + link['href'])
        soup = BeautifulSoup(page.text, "lxml")
        section = soup.find("section")
        scrap_synonym(section, name_list, not_found)
    else:
        not_found.append(specie)


def scrap_synonym(section_html, name_list, not_found):
    title = section_html.find("h1")
    subtitle = title.select_one(".subtitle")
    firstLink = subtitle.find("a")
    if(firstLink.text == "accepted"):
        name_list.append({
            "nome_passado": title.select_one(".name").text,
            "nome_correto": title.select_one(".name").text,
        })
    else:
        accepted_name = subtitle.find("span", class_="name")
        if(accepted_name):
            name_list.append({
                "nome_passado": title.select_one(".name").text,
                "nome_correto": accepted_name.text,
            })
        else:
            not_found.append(title.select_one(".name").text)


def scrap_info(source_html, specie, name_list, not_found):
    soup = BeautifulSoup(source_html, "lxml")
    section = soup.find("section")

    # Test if has more than one plant with the name
    header2 = section.find("h2")
    isResult = False
    if(header2 and header2.text == "Results"):
        return scrap_results(section, specie, name_list, not_found)
    return scrap_synonym(section, name_list, not_found)


def crawl_all_species(species, name_list, not_found):
    for specie in species:
        print(specie)
        page = requests.get(
            BASE_URL + "tpl1.1/search?q=" + util.normalize(specie))
        scrap_info(page.text, specie, name_list, not_found)


def getNames():
    with open(os.path.join(DIRNAME, 'data/florabrasil_NOTFOUND.json')) as f:
        species = json.load(f)

    name_list = []
    not_found = []
    crawl_all_species(species, name_list, not_found)

    with io.open(os.path.join(DIRNAME, 'data/plantlist_data.json'), 'w', encoding="UTF-8") as list_file:
        json.dump(name_list, list_file, indent=2, ensure_ascii=False)

    with io.open(os.path.join(DIRNAME, 'data/plantlist_NOTFOUND.json'), 'w', encoding="UTF-8") as list_file:
        json.dump(not_found, list_file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    getNames()
