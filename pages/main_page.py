from .base_page import BasePage
from .locators import BasePageLocators


class MainPage(BasePage):
    def add_item_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.FIRST_ITEM)
        link.click()
