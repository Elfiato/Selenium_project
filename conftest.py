import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Выберите браузер chrome или firefox, по умолчанию Google Chrome")
    parser.addoption('--headless', action='store', default='True',
                     help='Запуск браузера в фоновом режиме True или False, по умолчанию True')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption('headless')
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless == 'True':
            options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless == 'True':
            options.add_argument('--headless')
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
