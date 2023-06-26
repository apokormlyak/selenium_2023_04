from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class NewUser(BasePage):
    FIRST_NAME_FIELD = (By.NAME, 'firstname')
    LAST_NAME_FIELD = (By.NAME, 'lastname')
    EMAIL_FIELD = (By.NAME, 'email')
    PHONE_FIELD = (By.NAME, 'telephone')
    PASSWORD_FIELD = (By.NAME, 'password')
    PASSWORD_CONFIRM_FIELD = (By.NAME, 'confirm')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    AGREE_CHECKBOX = (By.NAME, "agree")

    def fill_personal_details(self, firstname, lastname, email, telephone):
        self.element(self.CONTINUE_BUTTON).\
            find_element(*self.FIRST_NAME_FIELD).send_keys(firstname)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(lastname)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.PHONE_FIELD).send_keys(telephone)
        return self

    def fill_password_fields(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD)\
            .send_keys(password)
        self.driver.find_element(*self.PASSWORD_CONFIRM_FIELD)\
            .send_keys(password)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        return self

    def submit(self):
        self.driver.find_element(*self.AGREE_CHECKBOX).click()
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        return self
