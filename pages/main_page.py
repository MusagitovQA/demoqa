from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base


class Main_page(Base):
    url = 'https://demoqa.com/automation-practice-form'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_name = "//input[@id='firstName']"
    last_name = "//input[@id='lastName']"
    user_email = "//input[@id='userEmail']"
    user_gender = "//input[@id='gender-radio-1']"

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_user_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_email)))

    def get_user_gender(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_gender)))




    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_user_email(self, user_email):
        self.get_user_email().send_keys(user_email)
        print("Input user email")

    def click_user_gender(self):
        self.get_user_gender().click()
        print("Select user gender")

    # Methods

    def input_form(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_first_name("standard_user")
        self.input_last_name("secret_sauce")
        self.input_user_email("mail@mail.com")
        self.click_user_gender()
        # self.assert_word(self.get_main_word(), 'Products')
