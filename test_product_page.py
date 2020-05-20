#task 4_3 step 2
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
#from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

import pytest
import time

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
#, link

#def test_guest_can_add_product_to_basket(browser):
    # ваша реализация теста

    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #page = ProductPage(browser, link)
    #page.open()
    #page.add_product_to_basket()

    #page.solve_quiz_and_get_code()
    #page.should_be_product_added_to_basket_by_name()
    #page.should_be_product_added_to_basket_by_cost()
    #page.test_guest_cant_see_success_message_after_adding_product_to_basket()
    #page.test_guest_cant_see_success_message()
    #page.test_message_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty()

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "Qwe123456789qwE"
        #открыть страницу регистрации
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        #зарегистрировать нового пользователя
        #page = LoginPage(browser, browser.current_url)

        page.register_new_user(email, password)
        #проверить, что пользователь залогинен
        page.should_be_authorized_user()
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        #time.sleep(5)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, browser.current_url)
        page.test_guest_cant_see_success_message()
        #assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESAGE), ('Success message is not present')
    def test_user_can_add_product_to_basket(self, browser):
        # ваша реализация теста
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, browser.current_url)
        #page.open()
        page.add_product_to_basket()
        page.should_be_product_added_to_basket_by_name()
        page.should_be_product_added_to_basket_by_cost()
