import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from . import constants


def test_constructor_transition(login, driver):
    WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
    driver.find_element(By.XPATH, constants.BUTTON_ENTRANCE_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
    driver.find_element(By.XPATH, constants.BUTTON_CONSTRUCTOR).click()
    assert driver.current_url == constants.MAIN_PAGE_URL

    driver.quit()


@pytest.mark.parametrize(
    'tab, tab_div',
    [
        ('Соусы', "//*[@id='root']/div/main/section[1]/div[1]/div[2]"),
        ('Булки', "//*[@id='root']/div/main/section[1]/div[1]/div[1]"),
        ('Начинки', "//*[@id='root']/div/main/section[1]/div[1]/div[3]"),
    ],
)
def test_constructor_tabs_transition(login, driver, tab, tab_div):
    driver.get(constants.MAIN_PAGE_URL)
    if tab == 'Булки':
        driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
    driver.find_element(By.XPATH, f"//span[text()='{tab}']").click()
    assert constants.ACTIVE_TAB_CLASS in driver.find_element(By.XPATH, tab_div).get_attribute("class")

    driver.quit()
