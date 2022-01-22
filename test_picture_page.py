from pages.picture_main_page import PicturePage
from pages.main_page import MainPage


def test_picture(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
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
