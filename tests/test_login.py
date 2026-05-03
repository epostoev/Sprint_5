from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthLocators
import data


class TestRegistration:

    def test_registrion_successful(self, driver):
        wait = WebDriverWait(driver, 10)
        # 1. Ждем отображение кнопки 'Вход и регистрация' и нажимает на кнопку
        wait.until(EC.visibility_of_element_located(
            MainPageLocators.LOGIN_REG_BUTTON)).click()
        # 2. Ждем отображения кнопки'Нет аккаунта' и нажимаем на кнопку
        wait.until(EC.visibility_of_element_located(
            AuthLocators.NO_ACCOUNT_BUTTON)).click()
        # 3. Заполняем поля формы
        email = data.generate_email()
        password = data.DEFAULT_PASSWORD
        wait.until(EC.visibility_of_element_located(
            AuthLocators.INPUT_EMAIL)).send_keys(email)
        wait.until(EC.visibility_of_element_located(
            AuthLocators.INPUT_PASSWORD)).send_keys(password)
        wait.until(EC.visibility_of_element_located(
            AuthLocators.INPUT_CONFIM_PASSWORD)).send_keys(password)
        driver.find_element(*AuthLocators.BUTTON_CREATE_ACCOUNT).click()

        wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.USER_AVATAR))
        assert driver.find_element(
            *MainPageLocators.USER_AVATAR) and driver.find_element(
            *MainPageLocators.LABEL_USER_NAME).text == "User."

    def test_registration_invalid_email_format(self, driver):
        wait = WebDriverWait(driver, 10)
        # 1. Ждем отображение кнопки 'Вход и регистрация' и нажимает на кнопку
        wait.until(EC.visibility_of_element_located(
            MainPageLocators.LOGIN_REG_BUTTON)).click()
        # 2. Ждем отображения кнопки'Нет аккаунта' и нажимаем на кнопку
        wait.until(EC.visibility_of_element_located(
            AuthLocators.NO_ACCOUNT_BUTTON)).click()
        # 3. Заполняем форму регистрации
        invalit_email = "invalid_format_email"
        wait.until(EC.visibility_of_element_located(
            AuthLocators.INPUT_EMAIL)).send_keys(invalit_email)
        # 4. Нажимает на создание аккаунта
        driver.find_element(*AuthLocators.BUTTON_CREATE_ACCOUNT).click()
        # 5. Находим элементы текста "Ошибка" и красные рамки вокруг полей
        # формы
        wait.until(EC.visibility_of_element_located(
            AuthLocators.EMAIL_ERROR_MESSAGE))
        error_massage = driver.find_element(
            *AuthLocators.EMAIL_ERROR_MESSAGE).text
        email_container = wait.until(EC.visibility_of_element_located(
            AuthLocators.FIELD_EMAIL_ERROR))
        border_color_email_container = email_container.value_of_css_property(
            'border-color')
        password_container = wait.until(EC.visibility_of_element_located(
            AuthLocators.FIELD_PASSWORD_ERROR))
        border_color_password_container = password_container.value_of_css_property(
            'border-color')
        confim_password_container = wait.until(
            EC.visibility_of_element_located(
                AuthLocators.FIELD_CONFIM_PASSWORD_ERROR))
        border_color_confim_password_container = confim_password_container.value_of_css_property(
            'border-color')
        # 6. Сравненение актуальных и ожидаемых значений
        assert (
            error_massage == "Ошибка") and (
            "255, 105, 114" in border_color_email_container) and (
            "255, 105, 114" in border_color_password_container) and (
                "255, 105, 114" in border_color_confim_password_container)

    def test_registration_already_exists_user(self, driver):
        wait = WebDriverWait(driver, 10)
        # 1. Ждем отображение кнопки 'Вход и регистрация' и нажимает на кнопку
        wait.until(EC.visibility_of_element_located(
            MainPageLocators.LOGIN_REG_BUTTON)).click()
        # 2. Ждем отображения кнопки'Нет аккаунта' и нажимаем на кнопку
        wait.until(EC.visibility_of_element_located(
            AuthLocators.NO_ACCOUNT_BUTTON)).click()
        # 3. Заполняем форму регистрации
        wait.until(EC.visibility_of_element_located(
            AuthLocators.INPUT_EMAIL)).send_keys(data.EXISTING_EMAIL)
        wait.until(EC.visibility_of_element_located(
            AuthLocators.INPUT_PASSWORD)).send_keys(data.EXISTING_PASSWORD)
        wait.until(
            EC.visibility_of_element_located(
                AuthLocators.INPUT_CONFIM_PASSWORD)).send_keys(
            data.EXISTING_PASSWORD)
        # 4. Нажимает на создание аккаунта
        driver.find_element(*AuthLocators.BUTTON_CREATE_ACCOUNT).click()
        # 5. Находим элементы текста "Ошибка" и красные рамки вокруг полей
        # формы
        wait.until(EC.visibility_of_element_located(
            AuthLocators.EMAIL_ERROR_MESSAGE))
        error_massage = driver.find_element(
            *AuthLocators.EMAIL_ERROR_MESSAGE).text
        email_container = wait.until(EC.visibility_of_element_located(
            AuthLocators.FIELD_EMAIL_ERROR))
        border_color_email_container = email_container.value_of_css_property(
            'border-color')
        password_container = wait.until(EC.visibility_of_element_located(
            AuthLocators.FIELD_PASSWORD_ERROR))
        border_color_password_container = password_container.value_of_css_property(
            'border-color')
        confim_password_container = wait.until(
            EC.visibility_of_element_located(
                AuthLocators.FIELD_CONFIM_PASSWORD_ERROR))
        border_color_confim_password_container = confim_password_container.value_of_css_property(
            'border-color')
        assert (
            error_massage == "Ошибка") and (
            "255, 105, 114" in border_color_email_container) and (
            "255, 105, 114" in border_color_password_container) and (
                "255, 105, 114" in border_color_confim_password_container)

    def test_login_user(self, driver):
        wait = WebDriverWait(driver, 10)
        # 1. Ждем отображение кнопки 'Вход и регистрация' и нажимает на кнопку
        wait.until(EC.visibility_of_element_located(
            MainPageLocators.LOGIN_REG_BUTTON)).click()
        # 2. Заполняем форму аунтификации
        wait.until(EC.visibility_of_element_located(
            AuthLocators.INPUT_EMAIL)).send_keys(data.EXISTING_EMAIL)
        wait.until(EC.visibility_of_element_located(
            AuthLocators.INPUT_PASSWORD)).send_keys(data.EXISTING_PASSWORD)
        # 3. Ждем отображения кнопки'Войти' и нажимаем на кнопку
        wait.until(EC.visibility_of_element_located(
            AuthLocators.BUTTON_ENTER)).click()
        wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.USER_AVATAR))
        assert driver.find_element(
            *MainPageLocators.USER_AVATAR) and driver.find_element(
            *MainPageLocators.LABEL_USER_NAME).text == "User."

    def test_logout_user(self, driver):
        wait = WebDriverWait(driver, 10)
        # 1. Ждем отображение кнопки 'Вход и регистрация' и нажимает на кнопку
        wait.until(EC.visibility_of_element_located(
            MainPageLocators.LOGIN_REG_BUTTON)).click()
        # 2. Заполняем форму аунтификации
        wait.until(EC.visibility_of_element_located(
            AuthLocators.INPUT_EMAIL)).send_keys(data.EXISTING_EMAIL)
        wait.until(EC.visibility_of_element_located(
            AuthLocators.INPUT_PASSWORD)).send_keys(data.EXISTING_PASSWORD)
        # 3. Ждем отображения кнопки'Войти' и нажимаем на кнопку
        wait.until(EC.visibility_of_element_located(
            AuthLocators.BUTTON_ENTER)).click()
        # 4. Ждем отображения кнопки'Выйти' и нажимаем на кнопку
        wait.until(EC.visibility_of_element_located(
            AuthLocators.BUTTON_EXIT)).click()

        avatar_disappeared = wait.until(
            EC.invisibility_of_element_located(MainPageLocators.USER_AVATAR))
        login_disappeared = wait.until(
            EC.invisibility_of_element_located(
                MainPageLocators.LABEL_USER_NAME))
        login_button_appeared = wait.until(EC.visibility_of_element_located(
            MainPageLocators.LOGIN_REG_BUTTON))
        assert avatar_disappeared and login_disappeared and login_button_appeared.text == "Вход и регистрация"
