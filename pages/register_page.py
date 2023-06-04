from .base_page import BasePage
from .locators import RegPageLocators
import time


class RegisterPage(BasePage):
    def register(self):
        self.browser.find_element(*RegPageLocators.REGISTER_BUTTON).click()
        self.browser.find_element(*RegPageLocators.EMAIL_FIELD).send_keys('test10534534636300765000@mail.ru')
        self.browser.find_element(*RegPageLocators.PASS_FIELD).send_keys('12235235325Aa')
        self.browser.find_element(*RegPageLocators.PASS_CONF_FIELD).send_keys('12235235325Aa')
        self.browser.find_element(*RegPageLocators.NAME_FIELD).send_keys('Александров Александр Александрович')
        self.browser.find_element(*RegPageLocators.PHONE_FIELD).send_keys('9000000000')
        time.sleep(1)
        self.browser.find_element(*RegPageLocators.PHONE_FIELD).send_keys('9000000000')
        self.browser.find_element(*RegPageLocators.REG_BUTTON).click()
        time.sleep(5)

    def login(self):
        self.browser.find_element(*RegPageLocators.LOGIN_EMAIL).send_keys('CORRECT EMAIL')
        self.browser.find_element(*RegPageLocators.EMAIL_BUTTON).click()
        self.browser.find_element(*RegPageLocators.LOGIN_PASS).send_keys('CORRECT PASSWORD')
        self.browser.find_element(*RegPageLocators.PASS_BUTTON).click()
