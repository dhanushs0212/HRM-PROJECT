
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import service


BaseUrl="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
username=" Admin"
password="admin123"

@pytest.fixture(scope="class",autouse=True)
def browser_setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    request.cls.driver = webdriver.chrome(ChromeDriverManager.install(),options=chrome_options)

    

