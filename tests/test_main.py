from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_smoke(driver):
    """
    Тестовый тест
    """
    driver.get("http://localhost:8080/index.html")
    navbar_text=driver.find_element(By.ID, "navbar-text") #проверка отображения
    my_photo=driver.find_element(By.ID, "my-photo")
   



    assert True, ""