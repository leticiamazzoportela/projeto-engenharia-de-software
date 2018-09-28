from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

BASE_URL = "http://www.theplantlist.org/"


def scrap_results(section_html, specie, name_list, not_found):
    item = section_html.find("td")
    if item:
        link = item.find("a")['href']
        page = requests.get(BASE_URL + link)
        soup = BeautifulSoup(page.text, "lxml")
        section = soup.find("section")
        scrap_synonym(section, name_list)
    else:
        not_found.append(specie)


def scrap_synonym(section_html, name_list):
    title = section_html.find("h1")
    subtitle = title.select_one(".subtitle")
    firstLink = subtitle.find("a")
    if(firstLink.text == "accepted"):
        name_list.append({
            "nome_passado": title.select_one(".name").text,
            "nome_correto": title.select_one(".name").text,
        })
    else:
        accepted_name = firstLink.findNext('a')
        name_list.append({
            "nome_passado": title.select_one(".name").text,
            "nome_correto": accepted_name.text,
        })


def scrap_info(source_html, specie, name_list, not_found):
    soup = BeautifulSoup(source_html, "lxml")
    section = soup.find("section")

    # Test if has more than one plant with the name
    header2 = section.find("h2")
    isResult = False
    if(header2 and header2.text == "Results"):
        return scrap_results(section, specie, name_list, not_found)
    return scrap_synonym(section, name_list)


def crawl_all_species(species, name_list, not_found):
    for specie in species:
        page = requests.get(BASE_URL + "tpl1.1/search?q=" + specie)
        scrap_info(page.text, specie, name_list, not_found)


def main():
    species = [
        "Hygrophila guianensis",
        "Hygrophila helodes",
        "Justicia comata",
        "Justicia aequilabris",
        "Justicia laevilinguis",
        "Justia pectoralis",
        "Nelsonia brunelloides",
        "Ruellia bahiensis",
        "Ruellia paniculata",
        "Sesuvium portulacastrum",
        "Echinodorus andrieuxii",
        "Echinodorus argentinensis",
        "Echinodorus aschersonianus",
        "Echinodorus bolivianus",
        "Echinodorus cordifolius",
    ]
    name_list = []
    not_found = []
    crawl_all_species(species, name_list, not_found)
    print(name_list)
    print("---------------\n", not_found)


main()
