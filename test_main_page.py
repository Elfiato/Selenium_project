from .pages.main_page import MainPage
from .pages.result_page import ResultPage


def test_search_site_in_search_engine(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_text_search_form()
    page.input_text()
    page.should_be_suggest()
    page.press_enter()
    result_page = ResultPage(browser, browser.current_url)
    result_page.should_be_search_result()
    result_page.find_link()
