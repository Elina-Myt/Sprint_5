import pytest
from links import Links
from locators import Locators


class TestConstructor:

    def test_ingredients_switch_buns(self, driver):

        # переход на главную страницу
        driver.get(Links.START_PAGE)

        # переключение разделов меню на "Начинки"
        driver.find_element(*Locators.FILLINGS_INGREDIENTS).click()

        # переключение разделов меню на "Булки"
        element = driver.find_element(*Locators.BUNS_INGREDIENTS)
        element.click()

        # получение атрибута класс элемента
        element_class = element.get_attribute('class')

        # проверка, что элемент меню выбран и это "Булки"
        assert 'current' in element_class and 'Булки' in element.text


    @pytest.mark.parametrize('ingredient, menu_title',
                             [[Locators.SAUCES_INGREDIENTS, 'Соусы'],
                              [Locators.FILLINGS_INGREDIENTS, 'Начинки']])
    def test_ingredients_switcher(self, driver, ingredient, menu_title):

        # переход на главную страницу
        driver.get(Links.START_PAGE)

        # переключение разделов меню
        element = driver.find_element(*ingredient)
        element.click()

        # получение атрибута класс элемента
        element_class = element.get_attribute('class')

        # проверка, что элемент меню выбран и название соответствует
        assert 'current' in element_class and menu_title in element.text