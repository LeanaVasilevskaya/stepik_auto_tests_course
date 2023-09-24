from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from pages.simple_button import SimpleBattonPage

class TestForm:

    def test_text_input_form_validation(self, browser):
        simple_page = SimpleBattonPage(browser)
        simple_page.open()
        text = browser.find_element(By.NAME, "text_string")
        text.click()
        text.send_keys('Liana_Vasilevskaya17-1996' +'\n')
