from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://www.theplantlist.org/"


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


def crawl_all_species(driver, species):
    global url
    last_url = url
    for specie in species:
        print(driver.current_url)
        text_field = driver.find_element_by_id('q')
        text_field.send_keys(specie)
        text_field.submit()

        WebDriverWait(driver, 15).until(
            lambda driver: driver.current_url != last_url)
        last_url = driver.current_url


def main():
    driver = get_driver()
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
    crawl_all_species(driver, species)
    sleep(1)


main()
