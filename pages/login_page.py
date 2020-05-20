from .base_page import BasePage
from .locators import LoginPageLocators
import time # в начале файла


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "слово login not in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login FORM is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register FORM is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password_field.send_keys(password)
        password_field_2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM_2)
        password_field_2.send_keys(password)
        reg_but = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_but.click()

