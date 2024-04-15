from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
def calc(num1, num2):
    return str(int(num1) + int(num2))

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    print(num1)
    num2 = browser.find_element(By.ID, "num2").text
    print(num2)
    x = calc(num1, num2)
    print(x)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(x)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    # time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()