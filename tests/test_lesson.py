from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
from selenium.webdriver.support.ui import WebDriverWait
browser = webdriver.Firefox()
import os


driver = webdriver.Firefox()
driver.get("http://suninjuly.github.io/explicit_wait2.html")
costs = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = browser.find_element(By.ID, "book")
button.click()





# time.sleep(1)
   # sumbit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
   # sumbit.click()
   # time.sleep(2)

   # text = i.text
   # c = calc(text)
   # v = browser.find_element(By.ID, "answer")
   # v.send_keys(c)
   # s = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
   # s.click()


































