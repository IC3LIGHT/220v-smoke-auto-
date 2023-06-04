from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def clear_basket(self):
        self.browser.find_element(*BasketPageLocators.DEL_BTN).click()

    def increase_item(self):
        self.browser.find_element(*BasketPageLocators.INCREASE_BTN).click()
