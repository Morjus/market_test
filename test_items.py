import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]

@pytest.mark.parametrize('link', links)
class TestMarketPage(object):

    def test_add_to_cart_button_exists(self,browser,link):
        wait = WebDriverWait(browser,15)
        browser.get(link)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'content')))
        assert browser.find_elements_by_id('add_to_basket_form'), 'No "Add to cart" button.'
