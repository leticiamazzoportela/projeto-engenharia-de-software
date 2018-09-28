from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

BASE_URL = "http://www.theplantlist.org/tpl1.1/search"


def scrap_results(section_html):
    pass


def scrap_synonym(section_html):
    title = section_html.find("h1")
    subtitle = title.select_one(".subtitle")
    firstLink = subtitle.find("a")
    if(firstLink.text == "accepted"):
        print(title.select_one(".name").text)
    else:
        accepted_name = firstLink.findNext('a')
        print(title.select_one(".name").text + ">>" + accepted_name.text)


def scrap_info(source_html):
    soup = BeautifulSoup(source_html, "lxml")
    section = soup.find("section")

    # Test if has more than one plant with the name
    header2 = section.find("h2")
    isResult = False
    if(header2 and header2.text == "Results"):
        return scrap_results(section)
    return scrap_synonym(section)


def crawl_all_species(species):
    for specie in species:
        page = requests.get(BASE_URL + "?q=" + specie)
        scrap_info(page.text)


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
    crawl_all_species(species)


main()
