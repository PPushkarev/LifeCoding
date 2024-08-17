
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from links import *
from base.base_page import BasePage

class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE
    SAVE_BUTTON = (By.CSS_SELECTOR, "div[class='oxd-form-actions'] button[class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']:nth-of-type(1)")
    INPUT_NAME  = (By.CSS_SELECTOR, "input[name='firstName']")


    def input_name (self):
        first_name = self.element_is_viasable(self.INPUT_NAME)
        previouse_name = first_name.get_attribute('value')
        first_name.clear()
        first_name.send_keys(Keys.CONTROL + "A")
        first_name.send_keys(Keys.BACKSPACE)
        first_name.send_keys('WOV')
        self.element_is_viasable(self.SAVE_BUTTON).click()
        current_name = first_name.get_attribute('value')
        return previouse_name, current_name






