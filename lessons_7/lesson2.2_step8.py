from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Ivan")
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input1.send_keys("Stepanov")
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input1.send_keys("test@test.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    print(current_dir)
    file_path = os.path.join(current_dir, "test")  # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

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