from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
button = browser.find_element_by_id('book')
button.click()

button1 = browser.find_element_by_id('solve')
browser.execute_script("return arguments[0].scrollIntoView(true);", button1)

value_x = browser.find_element_by_id('input_value').text
result = calc(value_x)
answer = browser.find_element_by_id('answer')
answer.send_keys(result)

button1.click()

time.sleep(10)
browser.quit()
