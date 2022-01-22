from selenium.webdriver.common.by import By


class MainPageLocators():
    SEARCH_TEXT_FORM = (By.CSS_SELECTOR, "#text")
    SEARCH_TEXT = 'Тензор'
    SUGGEST = (By.XPATH, '//*[contains(@id, "suggest-list")]')


class ResultPageLocators():
    REQ_URL = 'tensor.ru'
    SEARCH_RES = (By.CSS_SELECTOR, '#search-result')
    EVERY_SEARCH_RESULT = (By.CSS_SELECTOR, '#search-result > .serp-item a.OrganicTitle-Link')


class PicturePageLocators():
    FIRST_CATEGORY_URL = (By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0 a.Link')
    FIRST_CATEGORY = (By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0')
    PICTURE_MAIN_ICON = (By.CSS_SELECTOR, 'a.home-link[data-id="images"]')
    PICTURE_VALID_URL = 'https://yandex.ru/images/'
    PICTURE_SEARCH_STR = (By.CSS_SELECTOR, '.search2__input .input__box .input__control')
    FIRST_PICTURE_IN_SEARCH = (By.CSS_SELECTOR, '.serp-list_type_search .serp-item:nth-child(4) a')
    OPENED_PICTURE = (By.CSS_SELECTOR, '.MMImage-Origin')
    NEXT_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_next')
    PREV_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_prev')
