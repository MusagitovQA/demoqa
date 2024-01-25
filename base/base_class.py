import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):                 # Метод для отображения url
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):        # Проверка текста
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method Screenshot"""

    def get_screenshot(self):                    # Скриншот с добавлением даты времени
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\projectDemo\\screen\\' + name_screenshot)
