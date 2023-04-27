import pytest
import os.path
from selenium import webdriver
from selenium.webdriver.chrome import service


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--driver_folder', default='/home/alisapokormlyak/Desktop/drivers')
    parser.addoption('--url_opencart', default='http://192.168.1.6:8089/')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    driver_folder = request.config.getoption('--driver_folder')

    driver = None

    if browser_name.lower() == 'chrome':
        driver = webdriver.Chrome(executable_path=os.path.join(driver_folder, '/chromedriver'))
    elif browser_name.lower() == 'firefox':
        driver = webdriver.Firefox(executable_path=os.path.join(driver_folder, '/geckodriver'))
    elif browser_name.lower() == 'opera':
        webdriver_service = service.Service(executable_path=os.path.join(driver_folder, '/operadriver'))
        webdriver_service.start()
        capabilities = {
            'operaOptions': {
                'binary': '/usr/lib/x86_64-linux-gnu/opera'
            }
        }

        driver = webdriver.Remote(webdriver_service.service_url, capabilities)

    yield driver

    driver.close()


@pytest.fixture
def url(request):
    return request.config.getoption('--url_opencart')
