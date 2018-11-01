from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from contextlib import contextmanager
import time
from util import remove_author

url = "http://inct.splink.org.br/"


def wait_for(condition_function):
    start_time = time.time()
    while time.time() < start_time + 10:
        if condition_function():
            return True
        else:
            time.sleep(0.1)
    raise Exception('Timeout waiting for {}'.format(
        condition_function.__name__))


@contextmanager
def wait_for_page_load(browser, conditional=None):
    old_page = browser.find_element_by_tag_name('html')

    yield

    def page_has_loaded():
        new_page = browser.find_element_by_tag_name('html')
        return new_page.text != old_page.text

    wait_for(conditional if conditional else page_has_loaded)


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


def search_specie(driver, specie):
    print(specie)
    driver.find_element_by_id('searchFormCall').click()
    inputField = driver.find_element_by_name('ts_any')
    inputField.clear()
    inputField.send_keys(remove_author(specie))
    driver.find_element_by_xpath("//input[@value='buscar']").click()


def select_download(driver):
    start_time = time.time()
    dropdown = None
    while(True):
        try:
            driver.find_element_by_id("div_hint_action"
                                      )
        except:
            time.sleep(0.1)
            continue
        break
    dropdown = driver.find_element_by_id("div_hint_action"
                                         ).find_element_by_tag_name("table").find_element_by_tag_name("table"
                                                                                                      ).find_elements_by_tag_name("th")[-2].find_element_by_tag_name("select")
    for option in dropdown.find_elements_by_tag_name("option"):
        if option.text == "… dados completos":
            option.click()
            break

    while(True):
        try:
            driver.find_element_by_xpath("//input[@name='agree']").click()
        except:
            time.sleep(0.1)
            continue
        break


def crawl_all_species(driver, species):
    ocurrences = {}
    for specie in species:
        search_specie(driver, specie)
        # select_download(driver)
        ocurrences[specie] = get_all_occurrences(driver)
    return ocurrences


def get_all_occurrences(driver):
    occurences = []
    while(True):
        time_start = time.time()
        while(True):
            if time.time() > time_start + 5:
                return occurences
            try:
                driver.find_element_by_xpath(
                    '//div[contains(@class, "record")]')
            except:
                time.sleep(0.1)
                continue
            break
        records = driver.find_elements_by_xpath(
            '//div[contains(@class, "record")]')
        i = 1
        for record in records[1:]:
            ocurrence = {}
            try:
                la = record.find_element_by_class_name("lA")
                lo = record.find_element_by_class_name("lO")
                laContent = la.text.replace("[lat: ", "")
                loContent = lo.text.replace("long: ", "")
                ocurrence["lat"] = laContent
                ocurrence["long"] = loContent
            except:
                ocurrence["lat"] = None
                ocurrence["long"] = None

            try:
                collector = record.find_element_by_class_name("cL")
                ocurrence["collector"] = collector.text
            except:
                ocurrence["collector"] = None

            try:
                country = record.find_element_by_class_name("lC")
                ocurrence["country"] = country.text
            except:
                ocurrence["country"] = None

            try:
                state = record.find_element_by_class_name("lS")
                ocurrence["state"] = state.text
            except:
                ocurrence["state"] = None

            try:
                local = record.find_element_by_class_name("lP")
                ocurrence["local"] = local.text
            except:
                ocurrence["local"] = None

            try:
                date = record.find_element_by_class_name("cY")
                ocurrence["date"] = date.text
            except:
                ocurrence["date"] = None
            occurences.append(ocurrence)
        try:
            driver.find_element_by_xpath(
                '//img[@src="imgs/next_icon.png" and @title="próxima página"]').click()
        except Exception as ex:
            break

    return occurences


def get_data(species):
    driver = get_driver()
    ocurrences = crawl_all_species(driver, species)
    driver.close()

    return ocurrences


if __name__ == "__main__":
    print(get_data(["Dicliptera ciliaris", "Dyschoriste maranhonis", "Hygrophila costata"]))
