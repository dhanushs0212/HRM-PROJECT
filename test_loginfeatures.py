import pytest
from selenium.webdriver.support import wait
from webdriver_manager.core import driver

import hrmpages.loginpage


class BaseUrl:
    pass


@pytest.mark.usefixtures("browser_setup")
class test_login:

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.loginpage = hrmpages.loginpage.loginpage(self.driver)
        wait.WebDriverWait.until(driver)

    def test_valid_login(self):
        self.loginpage.login(username="admin", password="admin123")

    def teardown_class(self):
        self.driver.quit()