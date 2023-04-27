from selenium.webdriver.common.by import By
from conftest import url


class ProductPage:
    CONTENT = (By.ID, 'content')
    BUTTON_LIST_VIEW = (By.ID, 'list-view')
    BUTTON_GRID_VIEW = (By.ID, 'grid-view')
    PRODUCT_COMPARE_BTN = (By.PARTIAL_LINK_TEXT, 'Product Compare')
    INPUT_SORT = (By.ID, 'input-sort')
    INPUT_LIMIT = (By.ID, 'input-limit')
