from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from . import constants


def test_personal_account_go_to_main_page(login, driver):
    WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
    driver.find_element(By.XPATH, constants.BUTTON_ENTRANCE_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
    assert driver.current_url == constants.PROFILE_PAGE_URL

    driver.quit()

def test_personal_account_logout(login, driver):
    WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
    driver.find_element(By.XPATH, constants.BUTTON_ENTRANCE_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
    driver.find_element(By.XPATH, constants.BUTTON_LOGOUT_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
    assert driver.current_url == constants.LOGIN_PAGE_URL

    driver.quit()


