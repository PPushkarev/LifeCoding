from base.base_test import Basetest
import time

import allure
import pytest

from conftest import driver
from pages.dashboard_page import DashboardPage
from pages.login_page import loginPage
from pages.personal_page import PersonalPage


@pytest.fixture()
def precondition(driver):
    test_login = loginPage(driver)
    test_login.open()
    test_login.login()


class Test_feature(Basetest):



    @allure.feature('Testing login to the Website')
    class Test_loginonce:
        @allure.title('Checking login page')
        def test_login_once(self, driver):
            test_login = loginPage(driver)
            test_login.open()
            current_url1 = test_login.get_current_url()
            test_login.login()
            current_url2 = test_login.get_current_url()
            print(current_url1, current_url2)
            assert current_url1 != current_url2


@allure.feature('Testing Dashboard access')
class Test_Clicklink:
    @allure.title('Checking Dashboard')
    def test_click_link(self, driver, precondition):
        test_click = DashboardPage(driver)
        test_click.open()
        current_url1 = test_click.get_current_url()
        test_click.click_link()
        current_url2 = test_click.get_current_url()
        print(current_url1, current_url2)
        assert current_url1 != current_url2


@allure.feature('Testing changing Name')
class Test_ChangeName:
    @allure.title('Checking how to change name')
    def test_change_name(self, driver, precondition):
        change_name = PersonalPage(driver)
        change_name.open()
        previouse_name, current_name = change_name.input_name()
        assert previouse_name != current_name
