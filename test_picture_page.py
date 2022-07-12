from pages.picture_main_page import PicturePage
from pages.main_page import MainPage


def test_picture(browser):
    '''
    Тест на корректную работу кнопок "вперед" и "назад" при перелистывании картинок в "Яндекс Картинках".
    Шаги тест-кейса:
    1. Открытие главной страницы Яндекс (в браузере Firefox, появляется оповещение о прекращении поддержки браузера,
        которое необходимо закрыть);
    2. Переход в категорию картинок;
    3. Открытие первой категории;
    4. Открытие первой картинки;
    5. Переход на следующую картинку;
    6. Возвращение на предыдущую картинку;
    7. Проверка на соответствие изначально открытой картинки и картинки, полученной при возвращении.
    '''
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.if_yandex_notion()
    page.should_be_picture()
    page.go_to_picture()
    page.switch_tab()
    picture_page = PicturePage(browser, browser.current_url)
    picture_page.is_valid_url()
    category_name = picture_page.go_to_first_category()
    picture_page.is_valid_search_text(category_name)
    picture_page.open_first_picture_in_search()
    picture_page.should_be_opened_picture()
    picture_page.move_to_opened_picture()
    picture_page.should_be_next_button()
    prev_picture = picture_page.open_next_picture()
    picture_page.move_to_opened_picture()
    picture_page.should_be_prev_button()
    picture_page.open_prev_picture(prev_picture)
