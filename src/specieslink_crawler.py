from bs4 import BeautifulSoup
import requests
import time
from util import remove_author

BASE_URL = "http://www.splink.org.br/mod_perl/searchHint?ts_genus="


def get_driver():
    # don't load images
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference(
        'dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    # init the browser
    driver = webdriver.Firefox(firefox_profile=firefox_profile)
    driver.get(url)
    return driver


def crawl_all_species(species):
    ocurrences = {}
    for specie in species:
        config.l_plant["text"] = specie
        ocurrences[specie] = get_all_occurrences(remove_author(specie))
    return ocurrences


def crawl_all_records(records):
    ocurrences = []
    for record in records[1:]:
        ocurrence = {}
        ocurrence["filo"] = record.find(
            class_="tP").text.strip() if record.find(class_="tP") else ""
        ocurrence["familia"] = record.find(
            class_="tF").text.strip() if record.find(class_="tF") else ""
        ocurrence["ordem"] = record.find(
            class_="tO").text.strip() if record.find(class_="tO") else ""
        ocurrence["genero"] = record.find(
            class_="tGa").text.strip() if record.find(class_="tGa") else ""
        ocurrence["especie"] = record.find(
            class_="tEa").text.strip() if record.find(class_="tEa") else ""
        ocurrence["classe"] = record.find(
            class_="tC").text.strip() if record.find(class_="tC") else ""
        ocurrence["coletor"] = record.find(
            class_="cL").text.strip() if record.find(class_="cL") else ""
        ocurrence["lat"] = record.find(class_="lA").text.strip().replace(
            "[lat: ", "") if record.find(class_="lA") else ""
        ocurrence["long"] = record.find(class_="lO").text.strip().replace(
            "long: ", "") if record.find(class_="lO") else ""
        ocurrence["pais"] = record.find(
            class_="lC").text.strip() if record.find(class_="lC") else ""
        ocurrence["data"] = record.find(
            class_="cY").text.strip() if record.find(class_="cY") else ""
        ocurrences.append(ocurrence)
    return ocurrences


def get_all_occurrences(specie):
    offset = 0

    page = requests.post(BASE_URL, data={
        'ts_genus': specie,
        'offset': offset
    })

    soup = BeautifulSoup(str(page.text), "lxml")

    items = soup.find(id="div_hint_summary").find_all("ll")
    occurences = []

    if (len(items) < 3):
        return occurences

    while(offset < int(items[2].text)):
        offset += 100
        occurences += crawl_all_records(soup.find_all(class_="record"))
        page = requests.post(BASE_URL, data={
            'ts_genus': specie,
            'offset': offset
        })
        soup = BeautifulSoup(page.text, "lxml")

    return occurences


def get_data(species):
    return crawl_all_species(species)


if __name__ == "__main__":
    print(get_data(["Cipura paludosa"]))
