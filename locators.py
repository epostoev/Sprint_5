from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_REG_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    BUTTON_POST_AD = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    USER_AVATAR = (By.XPATH, "//*[contains(@class, 'svgSmall')]")
    LABEL_USER_NAME = (By.XPATH, "//*[contains(text(), 'User')]")
    BUTTON_USER_ACCAUNT = (By.XPATH, "//button[@class = 'circleSmall']")

class AuthLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//*[contains(text(), 'Нет аккаунта')]")
    INPUT_EMAIL = (By.XPATH, "//*[contains(@placeholder, 'Введите Email')]")
    INPUT_PASSWORD = (By.XPATH, "//*[contains(@placeholder, 'Пароль')]")
    INPUT_CONFIM_PASSWORD = (By.XPATH, "//*[contains(@placeholder, 'Повторите пароль')]")
    BUTTON_CREATE_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    BUTTON_ENTER = (By.XPATH, "//button[contains(text(), 'Войти')]")
    BUTTON_EXIT = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    FIELD_EMAIL_ERROR = (By.XPATH, "//div[contains(@class, 'input_inputError') and .//input[@name='email']]")
    FIELD_PASSWORD_ERROR = (By.XPATH, "//div[contains(@class, 'input_inputError') and .//input[@name='password']]")
    FIELD_CONFIM_PASSWORD_ERROR = (By.XPATH, "//div[contains(@class, 'input_inputError') and .//input[@name='submitPassword']]")
    EMAIL_ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Ошибка')]")
    POPUP_TITLE = (By.XPATH, "//*[contains(text(), 'Чтобы разместить')]")

class AddPostOrder:
    INPUT_NAME = (By.XPATH, "//*[@placeholder = 'Название']")
    INPUT_DESCRIPTIOM = (By.XPATH, "//*[@placeholder = 'Описание товара']")
    INPUT_PRICE = (By.XPATH, "//*[@placeholder = 'Стоимость']")
    INPUT_CATEGORY = (By.XPATH, "//input[@name='category']/following-sibling::button")
    INPUT_CITY = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CATEGORY_OPTION_AUTO = (By.XPATH, "//*[contains(text(), 'Авто')]")
    CATEGORY_OPTION_BOOKS = (By.XPATH, "//*[contains(text(), 'Книги')]")
    CATEGORY_OPTION_GARDEN = (By.XPATH, "//*[contains(text(), 'Садоводство')]")
    CATEGORY_OPTION_HOBBY = (By.XPATH, "//*[contains(text(), 'Хобби')]")
    CITY_OPTION_MOSCOW = (By.XPATH, "//*[contains(text(), 'Москва')]")
    CITY_OPTION_SP = (By.XPATH, "//*[contains(text(), 'Санкт-Петербург')]")
    CITY_OPTION_NS = (By.XPATH, "//*[contains(text(), 'Новосибирск')]")
    CITY_OPTION_EKAT = (By.XPATH, "//*[contains(text(), 'Екатеринбург')]")
    CITY_OPTION_NN = (By.XPATH, "//*[contains(text(), 'Нижний Новгород')]")
    CITY_OPTION_KAZAN = (By.XPATH, "//*[contains(text(), 'Казань')]")
    RADIO_USED = (By.XPATH, "//div[contains(@class, 'radioUnput_shell') and .//label[text() = 'Б/У']]//div[contains(@class, 'radioUnput_input')]")
    RADIO_NEW = (By.XPATH, "//div[contains(@class, 'radioUnput_shell') and .//label[text() = 'Новый']]//div[contains(@class, 'radioUnput_input')]")
    BUTTON_PUBLISH = (By.XPATH, "//button[text() ='Опубликовать']")

class ProfileLocators:
    MY_ADS_CARDS_TITLES = (By.XPATH, "//div[@class='card']//div[@class = 'about']//h2")
    PAGINATION_NEXT = (By.XPATH, "//button[contains(@class, 'arrowButton--right')]")