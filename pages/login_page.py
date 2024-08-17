from selenium.webdriver.common.by import By
from links import *
from base.base_page import BasePage


class loginPage(BasePage):
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SUBMIT = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
    PAGE_URL = Links.LOGIN_PAGE

    def login(self):
        self.element_is_viasable(self.NAME_INPUT).send_keys ('Admin')
        self.element_is_viasable(self.PASSWORD_INPUT).send_keys ('admin123')
        self.element_to_be_clickable(self.SUBMIT).click()











