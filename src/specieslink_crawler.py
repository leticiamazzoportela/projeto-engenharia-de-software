from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from contextlib import contextmanager
import time

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


def search_specie(driver):
    with wait_for_page_load(driver):
        driver.find_element_by_id('searchFormCall').click()
        inputField = driver.find_element_by_name('ts_any')
        inputField.clear()
        inputField.send_keys("teste")
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
    


def crawl_all_species(driver):
    global url
    last_url = url
    search_specie(driver)
    select_download(driver)

def get_data():
    driver = get_driver()
    crawl_all_species(driver)


get_data()
