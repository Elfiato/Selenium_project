from pages.main_page import MainPage
from pages.result_page import ResultPage


def test_search_site_in_search_engine(browser):
    '''
    Тест на наличие сайта компании в первых 5 результатах поиска Яндекс по запросу ее названия.
    В файле ./pages/locators.py, в переменных SEARCH_TEXT и REQ_URL хранятся название компании и сайт,
    проверяемый в результатах поиска.
    Шаги тест-кейса:
    1. Открытие главной страницы Яндекс (в браузере Firefox, появляется оповещение о прекращении поддержки браузера,
        которое необходимо закрыть);
    2. Ввод названия компании в поисковую строку;
    3. Поиск по запросу;
    4. Проверка на наличие сайта компании в первых пяти результатах выдачи.
    '''
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.if_yandex_notion()
    page.should_be_text_search_form()
    page.input_text()
    page.should_be_suggest()
    page.press_enter()
    result_page = ResultPage(browser, browser.current_url)
    result_page.should_be_search_result()
    result_page.find_link()
