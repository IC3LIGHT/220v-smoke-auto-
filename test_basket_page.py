import time

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage


class TestBasketPage:
    def test_clearing_basket(self, browser):
        link = "https://www.220-volt.ru/"
        page = MainPage(browser, link)
        page.open()
        page.add_item_to_basket()
        time.sleep(5)
        page.basket_item()
        page = BasketPage(browser, link)
        time.sleep(3)
        page.clear_basket()

    def test_increase_amount(self, browser):
        link = "https://www.220-volt.ru/"
        page = MainPage(browser, link)
        page.open()
        page.add_item_to_basket()
        time.sleep(5)
        page.basket_item()
        page = BasketPage(browser, link)
        time.sleep(3)
        page.increase_item()
