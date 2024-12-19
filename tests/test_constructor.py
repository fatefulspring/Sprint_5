import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from . import constants, locators


class TestConstructor:
    def test_constructor_transition(self, login, driver):
        WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
        driver.find_element(By.XPATH, locators.BUTTON_ENTRANCE_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
        driver.find_element(By.XPATH, locators.BUTTON_CONSTRUCTOR).click()
        assert driver.current_url == constants.MAIN_PAGE_URL


    @pytest.mark.parametrize('tab', ['Соусы', 'Начинки'])
    def test_constructor_tabs_transition(self, login, driver, tab):
        driver.get(constants.MAIN_PAGE_URL)
        driver.find_element(By.XPATH, locators.TAB_PATH.format(tab=tab)).click()
        assert constants.ACTIVE_TAB_CLASS in driver.find_element(
            By.XPATH, locators.TAB_PATH_TEMPLATE.format(tab)
        ).get_attribute("class")

    def test_constructor_tabs_transition_bun(self, login, driver):
        driver.get(constants.MAIN_PAGE_URL)
        driver.find_element(By.XPATH, locators.SAUCE_TAB_PATH).click()
        driver.find_element(By.XPATH, locators.TAB_PATH.format(tab='Булки')).click()
        assert constants.ACTIVE_TAB_CLASS in driver.find_element(
            By.XPATH, locators.TAB_PATH_TEMPLATE.format('Булки')
        ).get_attribute("class")
