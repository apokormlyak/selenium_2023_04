from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class CurrencyBox(BasePage):
    CURRENCY_BUTTON = (By.CLASS_NAME, "dropdown-toggle")
    EUR = (By.NAME, "EUR")
    GBP = (By.NAME, "GBP")
    USD = (By.NAME, "USD")

    def open_currency_box(self):
        ActionChains(self.driver).move_to_element(self.element)\
            .pause(0.5).click().perform()

    @property
    def eur(self):
        ActionChains(self.driver).move_to_element(self.EUR).click().perform()
        self.element(self.CURRENCY_BUTTON)
        return self

    @property
    def gbp(self):
        ActionChains(self.driver).move_to_element(self.GBP).click().perform()
        self.element(self.CURRENCY_BUTTON)
        return self

    @property
    def usd(self):
        ActionChains(self.driver).move_to_element(self.USD).click().perform()
        self.element(self.CURRENCY_BUTTON)
        return self
