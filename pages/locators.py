from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".header-panel-user-icon")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".header-panel-cart-icon")
    FAVOR_BUTTON = (By.CSS_SELECTOR, ".header-panel-fav-icon")
    FIRST_ITEM = (By.CSS_SELECTOR, '.delivery-date-ok.eccomerce-added')
    SEARCH_BAR = (By.CSS_SELECTOR, '.header-search-input')


class RegPageLocators:
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#reg")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#user_email")
    PASS_FIELD = (By.CSS_SELECTOR, "#password1")
    PASS_CONF_FIELD = (By.CSS_SELECTOR, "#password2")
    NAME_FIELD = (By.CSS_SELECTOR, "#user_fullname")
    PHONE_FIELD = (By.CSS_SELECTOR, "#user_phone")
    REG_BUTTON = (By.CSS_SELECTOR, '#register-submit-button')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#user_email')
    EMAIL_BUTTON = (By.XPATH, '//*[@id="enter-id-submit"]/button')
    LOGIN_PASS = (By.CSS_SELECTOR, "#user_password")
    PASS_BUTTON = (By.XPATH, '//*[@id="link_login"]')


class BasketPageLocators:
    ITEM_BASKET = (By.CSS_SELECTOR, ".btn-yellow-flat")
    CONT_SHOPPING = (By.CSS_SELECTOR, ".btn-light-yellow-flat")
    BASKET_ITEMS = (By.CSS_SELECTOR, '.table-item.ecommerce-tracked-cart-item')
    DEL_BTN = (By.CSS_SELECTOR, 'a.btn-del')
    INCREASE_BTN = (By.CSS_SELECTOR, '.ui-spinner-up')
