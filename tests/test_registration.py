from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from . import constants, helpers, locators



class TestRegistration:

    def test_registration(self, driver):
        driver.get(constants.REGISTRATION_PAGE_URL)
        driver.find_element(By.XPATH, locators.NAME_INPUT).send_keys(helpers.generate_name())
        driver.find_element(By.XPATH, locators.EMAIL_INPUT).send_keys(helpers.generate_email())
        driver.find_element(By.XPATH, locators.PASSWORD_INPUT).send_keys(helpers.generate_pass())
        driver.find_element(By.XPATH, locators.REGISTRATION_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
        assert driver.current_url == constants.LOGIN_PAGE_URL

    def test_registration_is_duplicated(self, driver):
        driver.get(constants.REGISTRATION_PAGE_URL)
        driver.find_element(By.XPATH, locators.NAME_INPUT).send_keys(constants.EXISTING_USER_NAME)
        driver.find_element(By.XPATH, locators.EMAIL_INPUT).send_keys(constants.EXISTING_EMAIL_USER)
        driver.find_element(By.XPATH, locators.PASSWORD_INPUT).send_keys(constants.EXISTING_PASSWORD_USER)
        driver.find_element(By.XPATH, locators.REGISTRATION_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.ERROR_DISCLAIMER)))
        assert driver.find_element(By.XPATH, locators.ERROR_DISCLAIMER).text == 'Такой пользователь уже существует'

    def test_registration_without_name(self, driver):
        driver.get(constants.REGISTRATION_PAGE_URL)
        driver.find_element(By.XPATH, locators.NAME_INPUT).send_keys('')
        driver.find_element(By.XPATH, locators.EMAIL_INPUT).send_keys(constants.EXISTING_EMAIL_USER)
        driver.find_element(By.XPATH, locators.PASSWORD_INPUT).send_keys(constants.EXISTING_PASSWORD_USER)
        driver.find_element(By.XPATH, locators.REGISTRATION_FORM_BUTTON).click()
        elements = driver.find_elements(By.XPATH, locators.ERROR_DISCLAIMER)
        assert len(elements) == 0

    def test_registration_without_at_in_email(self, driver):
        driver.get(constants.REGISTRATION_PAGE_URL)
        driver.find_element(By.XPATH, locators.NAME_INPUT).send_keys(constants.EXISTING_USER_NAME)
        driver.find_element(By.XPATH, locators.EMAIL_INPUT).send_keys(
            constants.EXISTING_EMAIL_USER.replace('@', ''))
        driver.find_element(By.XPATH, locators.PASSWORD_INPUT).send_keys(constants.EXISTING_PASSWORD_USER)
        driver.find_element(By.XPATH, locators.REGISTRATION_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.ERROR_DISCLAIMER)))
        assert driver.find_element(By.XPATH, locators.ERROR_DISCLAIMER).text == 'Такой пользователь уже существует'

    def test_registration_without_domain_in_email(self, driver):
        driver.get(constants.REGISTRATION_PAGE_URL)
        driver.find_element(By.XPATH, locators.NAME_INPUT).send_keys(constants.EXISTING_USER_NAME)
        driver.find_element(By.XPATH, locators.EMAIL_INPUT).send_keys(
            constants.EXISTING_EMAIL_USER.replace('gmail.com', ''))
        driver.find_element(By.XPATH, locators.PASSWORD_INPUT).send_keys(constants.EXISTING_PASSWORD_USER)
        driver.find_element(By.XPATH, locators.REGISTRATION_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.ERROR_DISCLAIMER)))
        assert driver.find_element(By.XPATH, locators.ERROR_DISCLAIMER).text == 'Такой пользователь уже существует'

    def test_registration_without_name_in_email(self, driver):
        driver.get(constants.REGISTRATION_PAGE_URL)
        driver.find_element(By.XPATH, locators.NAME_INPUT).send_keys(constants.EXISTING_USER_NAME)
        driver.find_element(By.XPATH, locators.EMAIL_INPUT).send_keys('@gmail.com')
        driver.find_element(By.XPATH, locators.PASSWORD_INPUT).send_keys(constants.EXISTING_PASSWORD_USER)
        driver.find_element(By.XPATH, locators.REGISTRATION_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.ERROR_DISCLAIMER)))
        assert driver.find_element(By.XPATH, locators.ERROR_DISCLAIMER).text == 'Такой пользователь уже существует'

    def test_registration_with_invalid_characters_in_email(self, driver):
        driver.get(constants.REGISTRATION_PAGE_URL)
        driver.find_element(By.XPATH, locators.NAME_INPUT).send_keys(constants.EXISTING_USER_NAME)
        driver.find_element(By.XPATH, locators.EMAIL_INPUT).send_keys(f'{constants.EXISTING_EMAIL_USER}$%')
        driver.find_element(By.XPATH, locators.PASSWORD_INPUT).send_keys(constants.EXISTING_PASSWORD_USER)
        driver.find_element(By.XPATH, locators.REGISTRATION_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.ERROR_DISCLAIMER)))
        assert driver.find_element(By.XPATH, locators.ERROR_DISCLAIMER).text == 'Такой пользователь уже существует'

    def test_registration_with_invalid_password(self, driver):
        driver.get(constants.REGISTRATION_PAGE_URL)
        driver.find_element(By.XPATH, locators.NAME_INPUT).send_keys(constants.EXISTING_USER_NAME)
        driver.find_element(By.XPATH, locators.EMAIL_INPUT).send_keys(constants.EXISTING_EMAIL_USER)
        driver.find_element(By.XPATH, locators.PASSWORD_INPUT).send_keys(constants.TOO_SHORT_PASSWORD)
        driver.find_element(By.XPATH, locators.REGISTRATION_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.ERROR_DISCLAIMER_PASSWORD)))
        assert driver.find_element(By.XPATH, locators.ERROR_DISCLAIMER_PASSWORD).text == 'Некорректный пароль'
