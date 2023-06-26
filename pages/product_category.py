from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductCategoryPage(BasePage):
    DROPDOWNS = (By.CLASS_NAME, "dropdown")
    DROPDOWN_MENU = (By.CLASS_NAME, 'dropdown-menu')
    DROPDOWN_INNER_LIST = (By.CLASS_NAME, 'list-unstyled')
    SEE_ALL_LINK = (By.CLASS_NAME, 'see-all')
