from distutils.cmd import Command

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10, poll_frequency=1)

    def open(self):
        self.driver.get(self.PAGE_URL)

    def check_opened(self):
        self.wait.until(EC.url_to_be(self.driver.current_url))

    def get_current_url(self):
        return self.driver.current_url

    def current_url(self):
        return self.execute(Command.GET_CURRENT_URL)['value']

    def element_to_be_clickable(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))


    def element_is_viasable(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))












        self.url = "https://www.Ya.ru/"

    def go_to_the_url(self, url):
        self.url = url
        self.driver.get(self.url)

    def element_present(self,locator, time=5):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator))

    def elements_are_present(self,locator, time=5):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator))

    def WebDriverWait(self, driver, time):
        pass







