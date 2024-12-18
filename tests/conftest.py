import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from . import constants


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


@pytest.fixture()
def login(driver):
    driver.get(constants.LOGIN_PAGE_URL)
    driver.find_element(By.XPATH, constants.LOGIN_EMAIL_INPUT).send_keys(constants.EXISTING_EMAIL_USER)
    driver.find_element(By.XPATH, constants.LOGIN_PASSWORD_INPUT).send_keys(constants.EXISTING_PASSWORD_USER)
    driver.find_element(By.XPATH, constants.BUTTON_ENTRANCE_IN_ENTRANCE_PAGE).click()
