from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class FirstTask(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.endpoint = 'button'
        self.button_locator = (By.XPATH, '//*[@id="first"]')
        self.result_locator = (By.XPATH, '//*[@id="result"][2]')

    def open_page(self):
        self.open(self.endpoint)

    def click_button_on_page(self):
        self.click_button(*self.button_locator)

    def get_result_text(self):
        return self.get_text(*self.result_locator)

