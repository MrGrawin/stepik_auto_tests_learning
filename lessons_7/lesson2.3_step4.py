from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, ".btn")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value").text
    x = calc(x_element)
    print(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(x)

    button2 = browser.find_element(By.CSS_SELECTOR, ".btn")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()