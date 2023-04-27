from selenium.webdriver.common.by import By


class NewUserPage:
    BREADCRUMB = (By.CLASS_NAME, "breadcrumb")
    FIRST_NAME_FIELD = (By.NAME, 'firstname')
    LAST_NAME_FIELD = (By.NAME, 'lastname')
    EMAIL_FIELD = (By.NAME, 'email')
    PHONE_FIELD = (By.NAME, 'telephone')
    PASSWORD_FIELD = (By.NAME, 'password')
    PASSWORD_CONFIRM_FIELD = (By.NAME, 'confirm')
    RADIO_INLINE = (By.CLASS_NAME, 'radio-inline')
