from .base_page import BasePage
from .locators import ProductPageLocators
import pytest
#import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        login_link.click()
        #time.sleep(1)

    def should_be_product_added_to_basket_by_name(self):
        #реализует проверку что товар добавлен в корзину, проверка имени в сообщение
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESAGE), ('Success message is not present')
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        in_message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESAGE).text
        assert product_name == in_message_name, f'"{product_name}" is not "{in_message_name}"'
        #time.sleep(1)

    def should_be_product_added_to_basket_by_cost(self):
        # реализует проверку что товар добавлен в корзину, проверка цены в корзине
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), ('Total cost message is not present')
        product_prise = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_prise == basket_cost, f'{product_prise} is not {basket_cost}'
        #time.sleep(1)

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESAGE), ('Success message is not present')

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESAGE), ('Success message is not present')

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESAGE), ('Success message is not present')






