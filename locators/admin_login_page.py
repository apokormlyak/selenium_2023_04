from selenium.webdriver.common.by import By


class AdminLoginPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    LOGO = (By.XPATH, "//img[@title='OpenCart']")
    LINK = (By.LINK_TEXT, "OpenCart")
