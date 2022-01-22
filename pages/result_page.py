from .base_page import BasePage
from .locators import ResultPageLocators


class ResultPage(BasePage):

    def should_be_search_result(self):
        assert self.is_element_visible(*ResultPageLocators.SEARCH_RES), 'Результаты поиска не найдены.'

    def find_link(self):
        find_url_flag = False
        # Будет работать если количество результатов на странице меньше 5.
        links = self.browser.find_elements(*ResultPageLocators.EVERY_SEARCH_RESULT)
        for link in links[:5]:
            url = link.get_attribute("href")
            if ResultPageLocators.REQ_URL in url:
                find_url_flag = True
                break
        assert find_url_flag, 'В первых 5 результатах ссылка не найдена.'
