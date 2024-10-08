from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SecondTask(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.endpoint = 'checkboxes/'

    def open_page(self):
        self.open(self.endpoint)

    def select_radio_button(self, value):
        self.click_radio_button(By.XPATH, f"//input[@type='radio' and @value='{value}']")

    def click_get_results_button(self):
        self.click_button(By.ID, 'radio_go')

    def get_results_text(self):
        return self.get_text(By.ID, 'radio_result')