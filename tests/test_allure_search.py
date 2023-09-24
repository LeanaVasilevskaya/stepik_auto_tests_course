import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from pages.simple_button import SimpleBattonPage
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_batton(browser):
    simple_page = SimpleBattonPage(browser)#берем класс SimpleBattonPage и так как там внутри иниуиализатор _init__(self, browser)
                                                                                 # то в круглых скобках передаем ему этот браузер
    simple_page.open()# используем метод open  из simple_button
    assert simple_page.batton_is_displeyed()# функция _is_displeyed из simple_button которая проверяет что кнопка видима

def test_batton_click(browser):
    simple_page = SimpleBattonPage(browser)
    simple_page.open()
    simple_page.click_button()
    assert 'Submitted'==simple_page.result_text
class TestForm:

    def test_text_input_form_validation(self, browser):
        simple_page = SimpleBattonPage(browser)
        simple_page.open()









