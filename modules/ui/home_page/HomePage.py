from base.SeleniumBaseClass import SeleniumBase
from modules.ui.home_page.home_page_locators import *
from modules.ui.home_page.home_page_data import *


class HomePage(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver=driver)

    def navigate_to_homepage(self):
        self.driver.get(homepage_url)

    def get_home_page_title(self):
        title = self.get_element(title_locator)
        return title

    def enter_valid_search_data(self):
        self.enter_value(valid_search_data,textbox_search)

    def enter_invalid_search_data(self):
        self.enter_value(invalid_search_data,textbox_search)

    def click_search_button(self):
        self.click_element(btn_search)

    def get_valid_product_locator(self):
        element = self.get_element(valid_product_locator)
        return element

    def get_no_product_message_locator(self):
        element = self.get_element(no_product_message)
        return element

    def enter_short_search_data(self):
        self.enter_value(short_search_data,textbox_search)

    def get_minimum_length_message_locator(self):
        element = self.get_element(min_length_warning_locator)
        return element

    def click_on_link_computers(self):
        self.click_element(link_computers)

    def get_computer_products(self):
        element = self.get_element(computer_products_page_title)
        return element

    def click_on_link_electronics(self):
        self.click_element(link_electronics)

    def get_electronics_products(self):
        element = self.get_element(electronics_products_page_title)
        return element

    def click_on_link_apparel(self):
        self.click_element(link_apparel)

    def get_apparel_products(self):
        element = self.get_element(apparel_products_page_title)
        return element

    def click_on_link_digital_downloads(self):
        self.click_element(link_digital_downloads)

    def get_digital_download_products(self):
        element = self.get_element(digital_downloads_products_page_title)
        return element

    def click_on_link_books(self):
        self.click_element(link_books)

    def get_books_products(self):
        element = self.get_element(books_products_page_title)
        return element

    def click_on_link_jewelry(self):
        self.click_element(link_jewelry)

    def get_jewelry_products(self):
        element = self.get_element(jewelry_products_page_title)
        return element

    def click_on_link_gift_cards(self):
        self.click_element(link_gift_cards)

    def get_gift_card_products(self):
        element = self.get_element(gift_card_products_page_title)
        return element

    def click_shoes(self):
        self.get_element_mouse_hover(link_apparel,link_shoes)

    def click_clothing(self):
        self.get_element_mouse_hover(link_apparel,link_shoes,link_clothing)

    def click_accessories(self):
        self.get_element_mouse_hover(link_apparel,link_shoes,link_clothing,link_accessories)

    def click_desktops(self):
        self.get_element_mouse_hover(link_computers, link_desktops)

    def click_notebooks(self):
        self.get_element_mouse_hover(link_computers,link_desktops,link_notebooks)

    def click_software(self):
        self.get_element_mouse_hover(link_computers, link_desktops, link_notebooks,link_software)

    def get_message_product_added_locator(self):
        element = self.get_element(message_product_added_locator)
        return element

    def click_on_link_wishlist(self):
        self.click_element(link_wishlist)



