# Sample Python Selenium Page Object Model Framework
# for web site https://opensource-demo.orangehrmlive.com/web/index.php/
## There are 3 Test cases classes when we test functional working of website in terms of  search of product,  login,  and register user 




The tech stack used in this project are:

    Python as the programming language for writing test code
    PIP3 as the build tool
    VSCode as the preferred IDE for writing python code.

Running tests
Type in Terminal this command:

     pytest -v -s
        

Make HTML report
Type in Terminal this command:

    allure serve allure_result

To create new allure Report 
Use this commnand:

      pytest --alluredir=allure_results



## Testing Login Page
```
class loginPage(BasePage):
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SUBMIT = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
    PAGE_URL = Links.LOGIN_PAGE

    def login(self):
        self.element_is_viasable(self.NAME_INPUT).send_keys ('Admin')
        self.element_is_viasable(self.PASSWORD_INPUT).send_keys ('admin123')
        self.element_to_be_clickable(self.SUBMIT).click()
```

## Testing Dashboard Page
```
from selenium.webdriver.common.by import By
from links import *
from base.base_page import BasePage
class DashboardPage(BasePage):
    PAGE_URL = Links.DASHBOARD
    MY_INFO_TAB = (By.XPATH, "//span[text()='My Info']")

    def click_link(self):
        self.element_to_be_clickable(self.MY_INFO_TAB).click()
```






## Testing Creating new Account
```

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
```




 ## Using Main function for base methods:
```
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
   ```   
## Using Standard POM for every Page of website:
```     

class loginPage(BasePage):
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SUBMIT = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
    PAGE_URL = Links.LOGIN_PAGE

    def login(self):
        self.element_is_viasable(self.NAME_INPUT).send_keys ('Admin')
        self.element_is_viasable(self.PASSWORD_INPUT).send_keys ('admin123')
        self.element_to_be_clickable(self.SUBMIT).click()

``` 
## Using annotations for classes: 


    class Basetest:
        dashboard_page:DashboardPage
        login_page: loginPage
        personal_page:PersonalPage

        @pytest.fixture(autouse=True)
        def setuo(self,request,driver):
            request.cls.driver= driver
            request.cls.dashboard_page= DashboardPage(driver)
            request.cls.login_page= loginPage(driver)
            request.cls.personal_page= PersonalPage(driver) ```


## Using attachment screenshot for allure reports: 



```
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




         