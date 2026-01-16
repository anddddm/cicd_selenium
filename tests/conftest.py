import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.server import LocalServer
import os

def pytest_addoption(parser):
    #Добавляем опции командной строки
    parser.addoption("--browser", action="store", default="chrome", 
                     help="Браузер для тестов: chrome, firefox")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Запуск в headless режиме")

@pytest.fixture(scope="session")
def local_server():
    """
    Запуск локального сервера для тестов
    """
    # Определяем путь к папке с сайтом
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    site_dir = os.path.join(base_dir, "site")
    
    server = LocalServer(port=8080, directory=site_dir)
    server.start()
    yield server
    server.stop()

@pytest.fixture
def driver(request, local_server):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser}")
    
    driver.implicitly_wait(10)#Устанавливаем неявные ожидания
    
    driver.get("http://localhost:8080/index.html")#Открываем локальный сайт
    
    yield driver
    
    driver.quit()

@pytest.fixture
def browser(request):
    return request.getfixturevalue("driver")