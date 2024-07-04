import faker
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from links import Links
from faker import Faker
faker = Faker()

class TestGoToPage:

    @pytest.mark.parametrize('page', [Links.START_PAGE, Links.PROFILE_PAGE, Links.FEED_PAGE])
    def test_go_to_profile_page(self, driver, page):

        NAME = faker.name()
        EMAIL = faker.email()
        PASSWORD = 'Ab12345678'

        # переход на страницу регистрации пользователя
        driver.get(Links.REGISTRATION_PAGE)

        # ожидание загрузки страницы пока не появится кнопка "Зарегистрироваться"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

        # регистрация пользователя
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys(NAME)
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(EMAIL)
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(PASSWORD)

        # ожидание, что кнопка "Зарегистрироваться" кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # ожидание загрузки страницы пока не появится кнопка "Войти"
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

        # авторизация пользователя
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).clear()
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).send_keys(EMAIL)
        driver.find_element(*Locators.PWD_AUTH_FIELD).clear()
        driver.find_element(*Locators.PWD_AUTH_FIELD).send_keys(PASSWORD)

        # ожидание, что кнопка "Войти" кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # ожидание выполнения авторизации пользователя
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

        # переход на страницу
        driver.get(page)

        # ожидание выполнения загрузки страницы - наличие кнопки "Личный кабинет"
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(Locators.PROFILE_LINK))

        # клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.PROFILE_LINK).click()

        # ожидание выполнения загрузки страницы Личного кабинета
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))

        # получение адрес текущей страницы
        current_url = driver.current_url

        # проверка, что текущий адрес страницы - личный кабинет
        assert '/account' in current_url

    def test_go_to_constructor_page_from_profile(self, driver):
        NAME = faker.name()
        EMAIL = faker.email()
        PASSWORD = 'Ab12345678'
        # переход на страницу регистрации пользователя
        driver.get(Links.REGISTRATION_PAGE)

        # ожидание загрузки страницы пока не появится кнопка "Зарегистрироваться"
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))

        # регистрация пользователя
        driver.find_element(*Locators.NAME_REGISTRATION_FIELD).send_keys(NAME)
        driver.find_element(*Locators.EMAIL_REGISTRATION_FIELD).send_keys(EMAIL)
        driver.find_element(*Locators.PWD_REGISTRATION_FIELD).send_keys(PASSWORD)

        # ожидание, что кнопка "Зарегистрироваться" кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # ожидание загрузки страницы пока не появится кнопка "Войти"
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

        # авторизация пользователя
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).clear()
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).send_keys(EMAIL)
        driver.find_element(*Locators.PWD_AUTH_FIELD).clear()
        driver.find_element(*Locators.PWD_AUTH_FIELD).send_keys(PASSWORD)

        # ожидание, что кнопка "Войти" кликабельна
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # ожидание выполнения авторизации пользователя
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

        # клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.PROFILE_LINK).click()

        # ожидание выполнения загрузки страницы Личного кабинета
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))

        # клик по кнопке Констурктор
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        # ожидание выполнения загрузки Главной страницы
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.TITLE))

        # получение адрес текущей страницы
        title = driver.find_element(*Locators.TITLE).text

        # проверка, что текущий адрес страницы - личный кабинет
        assert title == 'Соберите бургер'