from selenium.webdriver.common.by import By
from links import *
from base.base_page import BasePage
class DashboardPage(BasePage):
    PAGE_URL = Links.DASHBOARD


    MY_INFO_TAB = (By.XPATH, "//span[text()='My Info']")

    def click_link(self):
        self.element_to_be_clickable(self.MY_INFO_TAB).click()





