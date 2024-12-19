# constructor
SAUCE_TAB_PATH = "//span[text()='Соусы']"
TAB_PATH = "//span[text()='{tab}']"
TAB_PATH_TEMPLATE = "//span[text()='{}']/parent::div"

BUTTON_ENTRANCE_IN_ENTRANCE_PAGE = '//button[contains(@class, "button_button_type_primary") and text()="Войти"]'
BUTTON_ENTRANCE_PERSONAL_ACCOUNT = "//p[text()='Личный Кабинет']/parent::a"
BUTTON_LOGOUT_PERSONAL_ACCOUNT = "//button[text()='Выход']"
BUTTON_CONSTRUCTOR = '//a[contains(@class, "AppHeader_header__link__3D_hX") and .//p[text()="Конструктор"]]'

# registration
NAME_INPUT = '//label[text()="Имя"]/following-sibling::input[@type="text"]'
EMAIL_INPUT = '//label[text()="Email"]/following-sibling::input[@type="text"]'
PASSWORD_INPUT = '//label[text()="Пароль"]/following-sibling::input[@type="password"]'
REGISTRATION_FORM_BUTTON = "//button[contains(@class, 'button_button_type_primary') and text()='Зарегистрироваться']"
ERROR_DISCLAIMER_PASSWORD = "//p[text()='Некорректный пароль']"
ERROR_DISCLAIMER = "//p[text()='Такой пользователь уже существует']"

# entrance
BUTTON_ENTRANCE_IN_MAIN_PAGE = '//button[contains(text(), "Войти в аккаунт")]'
BUTTON_ENTRANCE = '//a[contains(text(), "Войти")]'
