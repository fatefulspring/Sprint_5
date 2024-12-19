import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from . import constants, locators


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(constants.LOGIN_PAGE_URL)
    driver.find_element(By.XPATH, locators.EMAIL_INPUT).send_keys(constants.EXISTING_EMAIL_USER)
    driver.find_element(By.XPATH, locators.PASSWORD_INPUT).send_keys(constants.EXISTING_PASSWORD_USER)
    driver.find_element(By.XPATH, locators.BUTTON_ENTRANCE_IN_ENTRANCE_PAGE).click()
