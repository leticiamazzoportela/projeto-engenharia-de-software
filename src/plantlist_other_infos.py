from bs4 import BeautifulSoup
import requests
import json
import util
import re
from config import config

BASE_URL = "http://www.theplantlist.org/"


def scrap_results(section_html, specie):
    # get the accepted item
    try:
        table = section_html.select_one("#tbl-results").find("tbody")
        pattern = r"^%s.*" % (specie.split()[0] + " " + specie.split()[1])
        regex = re.compile(pattern, re.IGNORECASE)
        items = table.findAll('tr')
        for item in items:
            link = item.find('td').find('a')
            if(regex.match(link.text) and item.find_all('td')[1].text == "Accepted"):
                page = requests.get(BASE_URL + link['href'])
                soup = BeautifulSoup(page.text, "lxml")
                return scrap_synonym(soup, specie)
    except Exception as e:
        print(e)
    
    return {"name": specie}



def scrap_synonym(soup, specie):
    section_html = soup.find("section")

    specieData = {}

    specieData["name"] = specie
    specieData["family"] = soup.find(class_="family").text
    specieData["hierarchy"] = soup.find(class_ = "majorgroup").text

    synonyms = []
    try:
        synonyms_table = soup.find("table", class_="names synonyms").find("tbody")
        for row in synonyms_table.find_all("tr"):
            columns = row.find_all("td")
            if (columns[1].text == "Synonym"):
                synonyms.append(columns[0].text)
    except:
        pass

    specieData["synonyms"] = synonyms

    return specieData

def scrap_info(source_html, specie):
    soup = BeautifulSoup(source_html, "lxml")
    section = soup.find("section")

    # Test if has more than one plant with the name
    header2 = section.find("h2")
    if(header2 and header2.text == "Results"):
        return scrap_results(soup, specie)
    return scrap_synonym(soup, specie)


def crawl_all_species(species):
    last_search = ""
    page = None
    data = []
    for specie in species:
        if (config and config.l_plant):
            config.l_plant["text"] = specie
        if(last_search != specie):
            last_search = specie
            page = requests.get(
                BASE_URL + "tpl1.1/search?q=" + util.normalize(specie))
        data.append(scrap_info(page.text, specie))
    return data


def getNames(species):
    species = crawl_all_species(species)

    return species


if __name__ == "__main__":
    plantlist_data = json.loads(open("data/plant_flora.json").read())
    data = getNames(util.get_list_plantlist_name(plantlist_data))

    with open('data/plantData.json', 'w') as outfile:
        json.dump(data, outfile)
