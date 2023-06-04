from .pages.main_page import MainPage
from .pages.register_page import RegisterPage


class TestRegisterPage:
    def test_guest_can_reg(self, browser):
        link = "https://www.220-volt.ru/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = RegisterPage(browser, link)
        page.register()

    def test_login(self, browser):
        link = "https://www.220-volt.ru/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = RegisterPage(browser, link)
        page.login()
