import allure
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
from selenium import webdriver

from data.urls import Urls
from web_locators import UIWorkerLocators


@allure.step('Открытие браузер')
@pytest.fixture(params=['chrome', 'firefox'])
def driver_do(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get(Urls.url_main)
    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1920, 1080)
        driver.get(Urls.url_main)
    yield driver
    driver.quit()


