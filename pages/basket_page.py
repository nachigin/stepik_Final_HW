from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
import pytest
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def should_be_basket_is_empty(self):
        # реализует проверку "Ожидаем, что есть текст о том что корзина пуста"
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), ('Basket is not empty by message')
        assert self.is_not_element_present(*BasketPageLocators.ITEM_MESSAGE), ('Basket is not empty by item')



