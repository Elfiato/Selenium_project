from .base_page import BasePage
from .locators import MainPageLocators, PicturePageLocators
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    def should_be_text_search_form(self):
        assert self.is_element_visible(*MainPageLocators.SEARCH_TEXT_FORM), 'Поле поиска не найдено.'

    def input_text(self):
        text = self.get_visible_element(*MainPageLocators.SEARCH_TEXT_FORM)
        text.send_keys(MainPageLocators.SEARCH_TEXT)

    def should_be_suggest(self):
        assert self.is_element_visible(*MainPageLocators.SUGGEST), 'Таблица с подсказками не появилась.'

    def press_enter(self):
        self.get_visible_element(*MainPageLocators.SEARCH_TEXT_FORM).send_keys(Keys.ENTER)

    def should_be_picture(self):
        assert self.is_element_visible(
            *PicturePageLocators.PICTURE_MAIN_ICON), 'Обьект "Картинки" на главной странице не найден.'

    def go_to_picture(self):
        if self.is_element_visible(*PicturePageLocators.PICTURE_MAIN_ICON):
            link = self.get_visible_element(*PicturePageLocators.PICTURE_MAIN_ICON)
            link.click()
        else:
            assert self.is_element_visible(
                *PicturePageLocators.PICTURE_MAIN_ICON), 'Обьект "Картинки" на главной странице не найден.'

    def switch_tab(self):
        window = self.browser.window_handles[1]
        new_window = self.browser.switch_to.window(window)
        return new_window

    def if_yandex_notion(self):
        if str(self.browser).split('.')[2] == 'firefox' and self.is_element_visible(*MainPageLocators.NOTIFICATION):
            close_btn = self.get_visible_element(*MainPageLocators.NOTIFICATION_CLOSE_BUTTON)
            close_btn.click()
