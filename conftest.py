import datetime
import allure
import pytest
from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.chrome.service import Service




@pytest.fixture(scope='function')
def driver():
    service = Service("C:\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    yield driver
    try:

        alert = driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException:
        # Если алерта нет, продолжаем выполнение
        pass
    attach = driver.get_screenshot_as_png()
    screenshot_name = f"Screenshot_{datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}"
    allure.attach(attach, name=screenshot_name, attachment_type=allure.attachment_type.PNG)
    driver.quit()



