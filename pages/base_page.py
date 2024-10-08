from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://savkk.github.io/selenium-practice/"

    def open(self, endpoint):
        self.driver.get(self.url + endpoint)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click_button(self, by, value):
        button = self.find_element(by, value)
        button.click()

    def get_text(self, by, value):
        element = self.find_element(by, value)
        return element.text


    def click_radio_button(self, by, value):
        radio_button = self.find_element(by, value)
        radio_button.click()

    def check_checkbox(self, by, value):
        checkbox = self.find_element(by, value)
        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_checkbox(self, by, value):
        checkbox = self.find_element(by, value)
        if checkbox.is_selected():
            checkbox.click()