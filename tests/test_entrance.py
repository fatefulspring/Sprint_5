from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from . import constants, locators


class TestEntrance:

    def test_entrance_main_page(self, driver):
        driver.get(constants.MAIN_PAGE_URL)
        driver.find_element(By.XPATH, locators.BUTTON_ENTRANCE_IN_MAIN_PAGE).click()
        driver.find_element(By.XPATH, locators.EMAIL_INPUT).send_keys(constants.EXISTING_EMAIL_USER)
        driver.find_element(By.XPATH, locators.PASSWORD_INPUT).send_keys(constants.EXISTING_PASSWORD_USER)
        driver.find_element(By.XPATH, locators.BUTTON_ENTRANCE_IN_ENTRANCE_PAGE).click()
        WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
        assert driver.current_url == constants.MAIN_PAGE_URL


    def test_entrance_personal_account(self, driver):
        driver.get(constants.MAIN_PAGE_URL)
        driver.find_element(By.XPATH, locators.BUTTON_ENTRANCE_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, locators.EMAIL_INPUT).send_keys(constants.EXISTING_EMAIL_USER)
        driver.find_element(By.XPATH, locators.PASSWORD_INPUT).send_keys(constants.EXISTING_PASSWORD_USER)
        driver.find_element(By.XPATH, locators.BUTTON_ENTRANCE_IN_ENTRANCE_PAGE).click()
        WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
        assert driver.current_url == constants.MAIN_PAGE_URL

    def test_entrance_registration_page(self, driver):
        driver.get(constants.REGISTRATION_PAGE_URL)
        driver.find_element(By.XPATH, locators.BUTTON_ENTRANCE).click()
        driver.find_element(By.XPATH, locators.EMAIL_INPUT).send_keys(constants.EXISTING_EMAIL_USER)
        driver.find_element(By.XPATH, locators.PASSWORD_INPUT).send_keys(constants.EXISTING_PASSWORD_USER)
        driver.find_element(By.XPATH, locators.BUTTON_ENTRANCE_IN_ENTRANCE_PAGE).click()
        WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
        assert driver.current_url == constants.MAIN_PAGE_URL

    def test_entrance_recover_password(self, driver):
        driver.get(constants.RECOVER_PASSWORD_PAGE_URL)
        driver.find_element(By.XPATH, locators.BUTTON_ENTRANCE).click()
        driver.find_element(By.XPATH, locators.EMAIL_INPUT).send_keys(constants.EXISTING_EMAIL_USER)
        driver.find_element(By.XPATH, locators.PASSWORD_INPUT).send_keys(constants.EXISTING_PASSWORD_USER)
        driver.find_element(By.XPATH, locators.BUTTON_ENTRANCE_IN_ENTRANCE_PAGE).click()
        WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
        assert driver.current_url == constants.MAIN_PAGE_URL
