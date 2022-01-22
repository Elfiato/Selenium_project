from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_visible(self, how, what):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((how, what)))
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((how, what)))
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def get_visible_element(self, how, what):
        if self.is_element_visible(how, what):
            return self.browser.find_element(how, what)
        else:
            assert self.is_element_visible(how, what), f'Элемент с локатором {how} :: {what} не найден'

    def get_present_element(self, how, what):
        if self.is_element_present(how, what):
            return self.browser.find_element(how, what)
        else:
            assert self.is_element_present(how, what), f'Элемент с локатором {how} :: {what} не найден'

    def move_to_present_element(self, how, what):
        action = ActionChains(self.browser)
        element = self.get_present_element(how, what)
        action.move_to_element(element).perform()
