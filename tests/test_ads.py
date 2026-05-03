from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthLocators, AddPostOrder, ProfileLocators
import data
from datetime import datetime
import time


class TestAdvertisement:
    def test_created_unauth(self, driver):
        wait = WebDriverWait(driver, 10)
        # 1. Ждем отображение кнопки 'Разместить обьявление' и нажимает на
        # кнопку
        wait.until(EC.visibility_of_element_located(
            MainPageLocators.BUTTON_POST_AD)).click()
        modal_header = wait.until(EC.visibility_of_element_located(
            AuthLocators.POPUP_TITLE))
        expected_text = "Чтобы разместить объявление, авторизуйтесь"
        assert modal_header.text == expected_text, f"Ожидался заголовок '{expected_text}', но получили '{expected_text}'"

    def test_created_ad_auth_user(self, driver):
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
        # 4. Ждем аватарку
        wait.until(EC.visibility_of_element_located(
            MainPageLocators.USER_AVATAR))
        # 5. Ждем отображение кнопки 'Разместить обьявление' и нажимает на
        # кнопку
        wait.until(EC.element_to_be_clickable(
            MainPageLocators.BUTTON_POST_AD)).click()
        # 6. Переходим к созданию обьявления
        ad_name = f"Велосипед_{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
        wait.until(EC.visibility_of_element_located(
            AddPostOrder.INPUT_NAME)).send_keys(ad_name)
        wait.until(EC.visibility_of_element_located(
            AddPostOrder.INPUT_DESCRIPTIOM)).send_keys("Катался один сезон")
        wait.until(EC.visibility_of_element_located(
            AddPostOrder.INPUT_PRICE)).send_keys("60000")
        wait.until(
            EC.element_to_be_clickable(
                AddPostOrder.INPUT_CATEGORY)).click()
        wait.until(
            EC.element_to_be_clickable(
                AddPostOrder.CATEGORY_OPTION_BOOKS)).click()
        wait.until(EC.element_to_be_clickable(AddPostOrder.INPUT_CITY)).click()
        wait.until(
            EC.element_to_be_clickable(
                AddPostOrder.CITY_OPTION_SP)).click()
        wait.until(EC.element_to_be_clickable(AddPostOrder.RADIO_USED)).click()
        wait.until(
            EC.element_to_be_clickable(
                AddPostOrder.BUTTON_PUBLISH)).click()
        wait.until(EC.invisibility_of_element(AddPostOrder.BUTTON_PUBLISH))
        wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.BUTTON_USER_ACCAUNT)).click()
        while True:
            # Ищем кнопку "вправо"
            next_button = wait.until(
                EC.visibility_of_element_located(
                    ProfileLocators.PAGINATION_NEXT))
            # Проверяем, заблокирована ли она (атрибут 'disabled')
            if next_button.get_attribute("disabled") is not None:
                break
            else:
                current_card = driver.find_element(
                    *ProfileLocators.MY_ADS_CARDS_TITLES)
                next_button.click()
                # Ждем, пока эта конкретная карточка исчезнет из DOM.
                # Это гарантирует, что страница начала обновляться.
                wait.until(EC.staleness_of(current_card))
                # 6. Ждем появления новых карточек на следующей странице
                wait.until(
                    EC.presence_of_all_elements_located(
                        ProfileLocators.MY_ADS_CARDS_TITLES))

        wait.until(
            EC.presence_of_all_elements_located(
                ProfileLocators.MY_ADS_CARDS_TITLES))
        # time.sleep(10)
        titles_elements = driver.find_elements(
            *ProfileLocators.MY_ADS_CARDS_TITLES)
        ad_titles_text = [el.text for el in titles_elements]
        assert ad_name in ad_titles_text
