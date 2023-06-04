import time

from .pages.main_page import MainPage


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "https://www.220-volt.ru/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_can_go_to_basket_page(self, browser):
        link = "https://www.220-volt.ru/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()

    def test_guest_can_go_to_favor_page(self, browser):
        link = "https://www.220-volt.ru/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_favor_page()

    def test_guest_add_item(self, browser):
        link = "https://www.220-volt.ru/"
        page = MainPage(browser, link)
        page.open()
        page.add_item_to_basket()

    def test_continue_shopping(self, browser):
        link = "https://www.220-volt.ru/"
        page = MainPage(browser, link)
        page.open()
        page.add_item_to_basket()
        time.sleep(5)
        page.continue_shopping()

    def test_go_to_basket_with_item(self, browser):
        link = "https://www.220-volt.ru/"
        page = MainPage(browser, link)
        page.open()
        page.add_item_to_basket()
        time.sleep(5)
        page.basket_item()

    def test_search(self, browser):
        link = "https://www.220-volt.ru/"
        page = MainPage(browser, link)
        page.open()
        page.search_bar()
        time.sleep(3)
