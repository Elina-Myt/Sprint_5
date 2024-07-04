from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from links import Links
from locators import Locators
import faker
from faker import Faker

faker = Faker()

class TestLogout:

    def test_go_to_profile_page(self, driver):
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
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # ожидание загрузки страницы пока не появится кнопка "Войти"
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

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
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(Locators.PROFILE_LINK))
        driver.find_element(*Locators.PROFILE_LINK).click()

        # ожидание выполнения загрузки страницы Личного кабинета
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))

        # клик по кнопке "Выход"
        driver.find_element(*Locators.EXIT_BUTTON).click()

        # ожидание, что выполнился logout
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

        # проверка, что выполнился выход и кнопка "Войти" отображается
        assert driver.find_element(*Locators.LOGIN_BUTTON).is_displayed()