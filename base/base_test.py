import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import loginPage
from pages.personal_page import PersonalPage


# анотация типов
class Basetest:

        dashboard_page:DashboardPage
        login_page: loginPage
        personal_page:PersonalPage

        @pytest.fixture(autouse=True)
        def setuo(self,request,driver):
            request.cls.driver= driver
            request.cls.dashboard_page= DashboardPage(driver)
            request.cls.login_page= loginPage(driver)
            request.cls.personal_page= PersonalPage(driver)








