import pytest
import math
import time
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_guest_can_go_to_login_page(browser):
   link = "http://selenium1py.pythonanywhere.com/"
   browser.get(link)
   go_to_login_page(browser)

def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
