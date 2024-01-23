import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.main_page import Main_page


def test_form():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start test")

    mp = Main_page(driver)
    mp.input_form()

    print("Finish Test")
    time.sleep(10)
    driver.quit()
