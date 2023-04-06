import os.path

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--driver_folders', default='/home/alisapokormlyak/Desktop/drivers')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    driver_folders = request.config.getoption('--driver_folders')

    driver = None

    if browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path=os.path.join(driver_folders, '/chromedriver'))
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(executable_path=os.path.join(driver_folders, '/geckodriver'))

    driver.maximize_window()

    yield driver

    driver.close()
