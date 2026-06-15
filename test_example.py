import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "latest")   # <<< меняем на latest
    options.set_capability("selenoid:options", {"enableVideo": False})
    options.set_capability("acceptInsecureCerts", True)
    
    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        options=options         
    )
    yield driver
    driver.quit()

def test_example(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
