import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.form_page import Form_page


def test_form():  # Настройки Chromedriver
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start test")  # Вывод на экран начало теста

    fp = Form_page(driver)  # Присваиваем класс Form_page переменной fp
    fp.input_form()  # Вызываем метод из  Form_page

    print("Finish Test")  # Вывод на экран конец теста
    time.sleep(10)  # Ожидание 10сек
    driver.quit()  # Закрываем драйвер
