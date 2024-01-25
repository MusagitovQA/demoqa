from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base


class Form_page(Base):
    url = 'https://demoqa.com/automation-practice-form'

    # Locators

    first_name = "firstName"
    last_name = "input[id='lastName']"
    user_email = "//input[@id='userEmail']"
    user_gender = "//label[normalize-space()='Male']"
    user_mobile = "//input[@id='userNumber']"
    date_birth = "//input[@id='dateOfBirthInput']"
    subjects = "//input[@id='subjectsInput']"
    user_hobbies = "//label[normalize-space()='Sports']"
    upload_pic = "//input[@id='uploadPicture']"
    curr_address = "//textarea[@id='currentAddress']"
    select_state = "//div[contains(text(),'Select State')]"
    state_input = "//input[@id='react-select-3-input']"
    select_city = "//div[contains(text(),'Select City')]"
    city_input = "//input[@id='react-select-4-input']"
    button_submit = "//button[normalize-space()='Submit']"
    main_word = "//div[@id='example-modal-sizes-title-lg']"

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.first_name)))  # Поиск First Name на странице с использованием селектора ID

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.last_name)))  # Поиск Last Name на странице с использованием селектора CSS

    def get_user_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_email)))  # Поиск User Email на странице с использованием селектора XPATH

    def get_user_gender(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_gender)))

    def get_user_mobile(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_mobile)))

    def get_date_birth(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_birth)))

    def get_subjects(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subjects)))

    def get_user_hobbies(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_hobbies)))

    def get_upload_pic(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.upload_pic)))

    def get_curr_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.curr_address)))

    def get_select_state(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_state)))

    def get_state_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.state_input)))

    def get_select_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_city)))

    def get_city_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_input)))

    def get_button_submit(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_submit)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def input_first_name(self, first_name):                                                # Функции для заполнения форм
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

    def input_user_mobile(self, user_mobile):
        self.get_user_mobile().send_keys(user_mobile)
        print("Input user mobile")

    def select_date_birth(self, date_birth):
        self.get_date_birth().click()
        self.get_date_birth().send_keys(Keys.CONTROL + "a")
        self.get_date_birth().send_keys(date_birth)
        self.get_date_birth().send_keys(Keys.RETURN)
        print("Select date birth")

    def input_subjects(self, subjects):
        self.get_subjects().send_keys(subjects)
        self.get_subjects().send_keys(Keys.RETURN)
        print("Input subjects")

    def click_user_hobbies(self):
        self.get_user_hobbies().click()
        print("Select user hobbies")

    def click_upload_pic(self):
        self.get_upload_pic().send_keys("C:\\projectDemo\\upload_file\\test_upload.png")                                # Путь к скриншоту для добавления в форму загрузки
        print("Click upload pic")

    def input_curr_address(self, curr_address):
        self.get_curr_address().send_keys(curr_address)
        print("Input curr address")

    def click_select_state(self):
        self.get_select_state().click()
        print("Select state")

    def click_state_input(self):
        self.get_state_input().send_keys(Keys.RETURN)
        print("Input state")

    def click_select_city(self):
        self.get_select_city().click()
        print("Select city")

    def click_city_input(self):
        self.get_city_input().send_keys(Keys.RETURN)
        print("Input city")

    def click_button_submit(self):
        self.get_button_submit().click()
        print("Click button submit")

    # Methods

    def input_form(self):
        with allure.step("Input Form"):
            self.driver.get(self.url)
            self.driver.fullscreen_window()
            self.get_current_url()
            self.input_first_name("Petrovich")
            self.input_last_name("Petr")
            self.input_user_email("mail@mail.com")
            self.click_user_gender()
            self.input_user_mobile("8999999999")
            self.select_date_birth("08 Feb 1994")
            self.input_subjects("Maths")
            self.click_user_hobbies()
            self.click_upload_pic()
            self.input_curr_address("пр. Нариманова, 1 стр 2, Ульяновск, Ульяновская обл., 432071")
            self.click_select_state()
            self.click_state_input()
            self.click_select_city()
            self.click_city_input()
            self.click_button_submit()
            self.assert_word(self.get_main_word(), 'Thanks for submitting the form')  # Проверка на заполнении форм
            self.get_screenshot()                                                           # Скрин-проверка об успешном прохождении
