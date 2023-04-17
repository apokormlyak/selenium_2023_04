from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators.admin_login_page import AdminLoginPage
from locators.home_page import HomePage
from locators.common_header import CommonHeader
from locators.product_category import ProductCategoryPage
from locators.product_page import ProductPage
from locators.new_user_page import NewUserPage


def test_admin_login_page(browser, url):
    browser.get(url=url+'admin/')
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(AdminLoginPage.SUBMIT_BUTTON))
    browser.find_element(*AdminLoginPage.USERNAME_INPUT)
    browser.find_element(*AdminLoginPage.PASSWORD_INPUT)
    browser.find_element(*AdminLoginPage.SUBMIT_BUTTON)
    browser.find_element(*AdminLoginPage.LOGO)
    browser.find_element(*AdminLoginPage.LINK)


def test_home_page(browser, url):
    browser.get(url=url)
    WebDriverWait(browser, 5)
    browser.find_element(*CommonHeader.LOGO)
    browser.find_element(*CommonHeader.SEARCH_INPUT)
    browser.find_element(*CommonHeader.SEARCH_BUTTON)
    browser.find_element(*CommonHeader.CART)
    browser.find_elements(*CommonHeader.DROPDOWNS)
    browser.find_element(*HomePage.CONTENT)


def test_new_user_page(browser, url):
    browser.get(url=url+'index.php?route=account/register')
    WebDriverWait(browser, 5)
    browser.find_element(*CommonHeader.LOGO)
    browser.find_element(*CommonHeader.SEARCH_INPUT)
    browser.find_element(*CommonHeader.SEARCH_BUTTON)
    browser.find_element(*CommonHeader.CART)
    browser.find_elements(*CommonHeader.DROPDOWNS)
    breadcrumbs = browser.find_elements(*NewUserPage.BREADCRUMB)
    for breadcrumb in breadcrumbs:
        breadcrumb.get_attribute('href')

    browser.find_elements(*NewUserPage.FIRST_NAME_FIELD)
    browser.find_elements(*NewUserPage.LAST_NAME_FIELD)
    browser.find_elements(*NewUserPage.EMAIL_FIELD)
    browser.find_elements(*NewUserPage.PHONE_FIELD)
    browser.find_elements(*NewUserPage.PASSWORD_FIELD)
    browser.find_elements(*NewUserPage.PASSWORD_CONFIRM_FIELD)


def test_product_category_page(browser, url):
    browser.get(url=url)
    WebDriverWait(browser, 5)
    browser.find_element(*CommonHeader.LOGO)
    browser.find_element(*CommonHeader.SEARCH_INPUT)
    browser.find_element(*CommonHeader.SEARCH_BUTTON)
    browser.find_element(*CommonHeader.CART)
    dropdowns = browser.find_elements(*ProductCategoryPage.DROPDOWNS)
    for dropdown in dropdowns:
        ActionChains(browser).move_to_element(dropdown).perform()
        WebDriverWait(browser, 3).until(EC.presence_of_element_located(ProductCategoryPage.DROPDOWN_MENU))
        list_items = browser.find_elements(*ProductCategoryPage.DROPDOWN_INNER_LIST)
        for item in list_items:
            item.get_attribute('href')
        browser.find_element(*ProductCategoryPage.SEE_ALL_LINK).get_attribute('href')


def test_product_page(browser, url):
    browser.get(url=url+'desktops/mac')
    WebDriverWait(browser, 5)
    browser.find_element(*CommonHeader.LOGO)
    browser.find_element(*CommonHeader.SEARCH_INPUT)
    browser.find_element(*CommonHeader.SEARCH_BUTTON)
    browser.find_element(*CommonHeader.CART)
    browser.find_element(*ProductPage.CONTENT)
    browser.find_element(*ProductPage.BUTTON_GRID_VIEW).click()
    browser.find_element(*ProductPage.BUTTON_LIST_VIEW).click()
    browser.find_element(*ProductPage.INPUT_SORT)
    browser.find_element(*ProductPage.INPUT_LIMIT)
    browser.find_element(*ProductPage.PRODUCT_COMPARE_BTN).click()

















