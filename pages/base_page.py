from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_BUTTON)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        link.click()

    def go_to_favor_page(self):
        link = self.browser.find_element(*BasePageLocators.FAVOR_BUTTON)
        link.click()

    def continue_shopping(self):
        link = self.browser.find_element(*BasketPageLocators.CONT_SHOPPING)
        link.click()

    def basket_item(self):
        link = self.browser.find_element(*BasketPageLocators.ITEM_BASKET)
        link.click()

    def search_bar(self):
        link = self.browser.find_element(*BasePageLocators.SEARCH_BAR)
        link.send_keys('молоток')
