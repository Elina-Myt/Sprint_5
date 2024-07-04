import pytest
import selenium
from selenium.webdriver.common.by import By


class Locators:

    # страница регистрации пользователя
    NAME_REGISTRATION_FIELD = By.XPATH, ".//label[text()='Имя']/following-sibling::input"  # поле ввода имени
    EMAIL_REGISTRATION_FIELD = By.XPATH, ".//label[text()='Email']/following-sibling::input"  # поле ввода email
    PWD_REGISTRATION_FIELD = By.XPATH, ".//input[@type = 'password']"  # поле ввода пароля
    REGISTRATION_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']"  # кнопка "Зарегистрироваться"

    # страница авторизации пользователя
    EMAIL_AUTH_FIELD = By.XPATH, ".//*[text()='Email']/following-sibling::input"  # поле ввода email
    PWD_AUTH_FIELD = By.XPATH, ".//input[@type = 'password']"  # поле ввода пароля
    LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти']"  # кнопка "Войти"
    WRONG_PASSWORD_TEXT = By.CLASS_NAME, "input__error"  # сообщение об ошибке ввода пароля

    # главная страница
    LOGIN_BUTTON_FROM_MAIN_PAGE = By.XPATH, ".//button[text()='Войти в аккаунт']"  # кнопка "Войти в аккаунт"
    ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"  # кнопка "Оформить заказ"
    CONSTRUCTOR_BUTTON = By.LINK_TEXT, "Конструктор"  # кнопка "Конструктор"
    TITLE = By.CLASS_NAME, "text_type_main-large"  # заголовок Главной страницы

    # Личный кабинет
    PROFILE_LINK = By.LINK_TEXT, "Личный Кабинет"  # кнопка перехода в Личный кабинет
    LOGIN_LINK = By.LINK_TEXT, "Войти"  # ссылка на страницу авторизации
    EXIT_BUTTON = By.XPATH, ".//button[text()='Выход']"  # кнопка "Выход"

    # Констурктор
    BUNS_INGREDIENTS = By.XPATH, ".//span[text()='Булки']/parent::div"  # пункт меню "Булки"
    SAUCES_INGREDIENTS = By.XPATH, ".//span[text()='Соусы']/parent::div"  # пункт меню "Соусы"
    FILLINGS_INGREDIENTS = By.XPATH, ".//span[text()='Начинки']/parent::div"  # пункт меню "Начинки"
    SELECTED_INGREDIENTS = By.XPATH, ".//*[starts-with(@class, 'tab_tab') and contains(@class, 'current')]"  # выбранный пункт меню