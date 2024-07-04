from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from links import Links
import faker
from faker import Faker

faker = Faker()


class TestLogin:

    def test_login_button_from_main_page(self, driver):

        # переход на главную страницу
        driver.get(Links.START_PAGE)

        # клик по кнопке "Войти в аккаунт"
        driver.find_element(*Locators.LOGIN_BUTTON_FROM_MAIN_PAGE).click()

        # получение адрес текущей страницы
        current_url = driver.current_url

        # проверка, что текущий адрес страницы - страниц авторизации
        assert '/login' in current_url


    def test_login_button_from_profile(self, driver):

        # переход на главную страницу
        driver.get(Links.START_PAGE)

        # клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.PROFILE_LINK).click()

        # получение адрес текущей страницы
        current_url = driver.current_url

        # проверка, что текущий адрес страницы - страниц аавторизации
        assert '/login' in current_url


    def test_login_button_registration_page(self, driver):

        # переход на страницу регистрации
        driver.get(Links.REGISTRATION_PAGE)

        # клик по ссылке "Войти"
        driver.find_element(*Locators.LOGIN_LINK).click()

        # получение адрес текущей страницы
        current_url = driver.current_url

        # проверка, что текущий адрес страницы - страниц аавторизации
        assert '/login' in current_url


    def test_login_success(self, driver):
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
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.REGISTRATION_BUTTON))
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # ожидание загрузки страницы пока не появится кнопка "Войти"
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

        # авторизация пользователя
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).clear()
        driver.find_element(*Locators.EMAIL_AUTH_FIELD).send_keys(EMAIL)
        driver.find_element(*Locators.PWD_AUTH_FIELD).clear()
        driver.find_element(*Locators.PWD_AUTH_FIELD).send_keys(PASSWORD)

        # ожидание, что кнопка "Войти" кликабельна
        WebDriverWait(driver, 8).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # ожидание выполнения авторизации пользователя
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

        # клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.PROFILE_LINK).click()

        # получение адрес текущей страницы
        current_url = driver.current_url

        # проверка, что текущий адрес страницы - личный кабинет
        assert '/account' in current_url