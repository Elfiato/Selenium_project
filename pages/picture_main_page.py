from .base_page import BasePage
from .locators import PicturePageLocators


class PicturePage(BasePage):

    def go_to_first_category(self):
        if self.is_element_visible(*PicturePageLocators.FIRST_CATEGORY_URL):
            category = self.get_visible_element(*PicturePageLocators.FIRST_CATEGORY_URL)
            category_name = self.get_visible_element(*PicturePageLocators.FIRST_CATEGORY).get_attribute(
                'data-grid-text')
            print(f'Открываем категорию: {category_name}')
            category.click()
        assert self.is_element_visible(*PicturePageLocators.FIRST_CATEGORY_URL), 'Первая категория картинок не найдена.'
        return category_name

    def is_valid_url(self):
        self.is_element_visible(*PicturePageLocators.FIRST_CATEGORY_URL)
        current_url = self.browser.current_url
        print(f'URL картинок: {current_url}')
        assert current_url.startswith(
            PicturePageLocators.PICTURE_VALID_URL), 'Текущий URl не совпадает с верным URL картинок'

    def is_valid_search_text(self, category_name):
        search_text = self.get_visible_element(*PicturePageLocators.PICTURE_SEARCH_STR).get_attribute('value')
        print(f'В строке поиска текст: {category_name}')
        assert category_name == search_text, 'Текст в строке поиска не соответсвует названию категории'

    def open_first_picture_in_search(self):
        if self.is_element_visible(*PicturePageLocators.FIRST_PICTURE_IN_SEARCH):
            self.get_visible_element(*PicturePageLocators.FIRST_PICTURE_IN_SEARCH).click()
        else:
            assert self.is_element_visible(
                *PicturePageLocators.FIRST_PICTURE_IN_SEARCH), 'Не найдено картинок доступных для открытия.'

    def should_be_opened_picture(self):
        assert self.is_element_present(*PicturePageLocators.OPENED_PICTURE), 'Картинка из поиска не открылась.'

    def open_next_picture(self):
        if self.is_element_visible(*PicturePageLocators.NEXT_BUTTON):
            prev_picture_url = self.get_present_element(*PicturePageLocators.OPENED_PICTURE)
            pic_url = prev_picture_url.get_attribute('src')
            self.get_visible_element(*PicturePageLocators.NEXT_BUTTON).click()
            print(f'Ссылка на первую открытую картинку: {pic_url}')
            return pic_url
        else:
            assert self.is_element_visible(
                *PicturePageLocators.NEXT_BUTTON), 'Кнопка открытия следующей картинки при переходе не найдена.'

    def open_prev_picture(self, prev_url):
        if self.is_element_visible(*PicturePageLocators.PREV_BUTTON):
            next_pic_url = self.get_present_element(*PicturePageLocators.OPENED_PICTURE).get_attribute('src')
            print(f'Ссылка на следующую открытую картинку: {next_pic_url}')
            self.get_visible_element(*PicturePageLocators.PREV_BUTTON).click()
            current_picture_url = self.get_present_element(*PicturePageLocators.OPENED_PICTURE)
            pic_url = current_picture_url.get_attribute('src')
            print(f'Ссылка на картинку при возвращении назад: {pic_url}')
            assert pic_url == prev_url, 'Предыдущая картинка несвпадает с запомненной.'
        else:
            assert self.is_element_visible(
                *PicturePageLocators.PREV_BUTTON), 'Кнопка открытия предыдущей картинки при переходе не найдена.'

    def should_be_next_button(self):
        assert self.is_element_visible(
            *PicturePageLocators.NEXT_BUTTON), 'Кнопка открытия следующей картинки не найдена.'

    def should_be_prev_button(self):
        assert self.is_element_visible(
            *PicturePageLocators.PREV_BUTTON), 'Кнопка открытия предыдущей картинки не найдена.'

    def move_to_opened_picture(self):
        self.move_to_present_element(*PicturePageLocators.OPENED_PICTURE)
