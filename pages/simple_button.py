from pages.base_page import BasePage
from selenium.webdriver.common.by import By

button_selector = (By.ID, 'submit-id-submit')# записали способ по которому будем искать "селектор"
result_selector = (By.ID, 'result-text')


class SimpleBattonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/input/simple') #метод для открытия нужной страницы(этот
                                                                                #метод потом используем в тексте

    def button(self):
        return self.find(button_selector)# передали селектор сюда

    #isDisplayed() //возвращает false, если элемент либо невидимый, либо его нет в DOM.
    # exists() //возвращает true, если элемент есть в DOM, иначе - false.
    def batton_is_displeyed(self):            #данная функция возвращает не баттон а статус, если кнопка видима True
        return self.button().is_displayed()

    def result(self):
        return self.find(result_selector)

    def click_button(self):
        self.button().click(), self.batton_is_displeyed()
    @property #если стоит проперти,то к методу можно обращаться просто как к переменной
    def result_text(self):       #метод который возвращает текст
        return self.result().text

