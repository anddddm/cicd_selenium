from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_smoke(driver):
    """
    Простой тест для github actions
    """
    driver.get("http://localhost:8080/index.html")
    navbar_text=driver.find_element(By.ID, "navbar-text") #проверка отображения
    my_photo=driver.find_element(By.ID, "my-photo")
    contacts_navbar=driver.find_element(By.ID, "contacts_navbar")
   


    assert True, ""