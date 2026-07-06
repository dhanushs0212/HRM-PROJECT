from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from hrm_helper.selenium_helper import SeleniumHelper


class LoginPage(SeleniumHelper):
    email_webelement = (By.XPATH, "//input[@name='username']")
    password_webelement = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        self.webelement_enter(self.email_webelement, username)

    def enter_password(self, password):
        self.webelement_enter(self.password_webelement, password)

    def click_login(self):
        self.webelement_click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")

    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")