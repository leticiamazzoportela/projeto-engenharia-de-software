from bs4 import BeautifulSoup
import requests
import json
import util
import re

BASE_URL = "http://www.theplantlist.org/"


def scrap_results(section_html, specie):
    # get the accepted item
    try:
        table = section_html.select_one("#tbl-results").find("tbody")
        pattern = r"^%s.*" % (specie["nome"].split()[0] + " " + specie["nome"].split()[1])
        regex = re.compile(pattern, re.IGNORECASE)
        items = table.findAll('tr')
        for item in items:
            link = item.find('td').find('a')
            if(regex.match(link.text)):
                page = requests.get(BASE_URL + link['href'])
                soup = BeautifulSoup(page.text, "lxml")
                section = soup.find("section")
                return scrap_synonym(section, specie)
    except:
        specie["status_plantlist"] = "nao_encontrado"
        specie["plantlist"] = ""



def scrap_synonym(section_html, specie):
    title = section_html.find("h1")
    subtitle = title.select_one(".subtitle")
    firstLink = subtitle.find("a")
    if(firstLink.text == "accepted"):
        specie["status_plantlist"] = ""
        specie["plantlist"] = title.select_one(".name").text
    elif (firstLink.text == "synonym"):
        accepted_name = subtitle.find("span", class_="name")
        if(accepted_name):
            specie["status_plantlist"] = "sinonimo"
            specie["plantlist"] = accepted_name.text
    else:
        specie["status_plantlist"] = "Não resolvido"
        specie["plantlist"] = title.select_one(".name").text


def scrap_info(source_html, specie):
    soup = BeautifulSoup(source_html, "lxml")
    section = soup.find("section")

    # Test if has more than one plant with the name
    header2 = section.find("h2")
    if(header2 and header2.text == "Results"):
        return scrap_results(section, specie)
    return scrap_synonym(section, specie)


def crawl_all_species(species):
    last_search = ""
    page = None
    for specie in species:
        print(specie["nome"])
        first_name = specie["nome"].split()[0]
        if(last_search != first_name):
            last_search = first_name
            page = requests.get(
                BASE_URL + "tpl1.1/search?q=" + util.normalize(first_name))
        scrap_info(page.text, specie)


def getNames(species):

    crawl_all_species(species)

    return species


if __name__ == "__main__":
    species = getNames([
        {
            "nome": "Dicliptera ciliaris Juss."
        },
        {
            "nome": "Dyschoriste maranhonis Kuntze"
        },
        {
            "nome": "Hygrophila costata Nees"
        },
        {
            "nome": "Hygrophila angusta"
        },
        {
            "nome":"Justia pectoralis Jacq."
        }
    ])

    print(species)
