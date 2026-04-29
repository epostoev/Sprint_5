from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_REG_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    POST_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить обьявление')]")
    USER_AVATAR = (By.XPATH, "//*[contains(@class, 'svgSmall')]")
    LABEL_USER_NAME = (By.XPATH, "//*[contains(text(), 'User')]")

class AuthLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//*[contains(text(), 'Нет аккаунта')]")
    INPUT_EMAIL = (By.XPATH, "//*[contains(@placeholder, 'Введите Email')]")
    INPUT_PASSWORD = (By.XPATH, "//*[contains(@placeholder, 'Пароль')]")
    INPUT_CONFIM_PASSWORD = (By.XPATH, "//*[contains(@placeholder, 'Повторите пароль')]")
    BUTTON_CREATE_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")


