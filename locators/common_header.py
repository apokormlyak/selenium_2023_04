from selenium.webdriver.common.by import By


class CommonHeader:
    LOGO = (By.CSS_SELECTOR, "#logo")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='button']")
    CART = (By.ID, "cart")
    DROPDOWNS = (By.CLASS_NAME, "dropdown")
