import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthLocators
import data
from selenium.webdriver.common.by import By
from selenium import webdriver


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
        input()
        assert driver.find_element(
            *
            MainPageLocators.USER_AVATAR) and driver.find_element(
            *
            MainPageLocators.LABEL_USER_NAME).text == "User."
