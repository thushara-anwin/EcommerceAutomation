from base.SeleniumBaseClass import SeleniumBase
from modules.ui.cellphones.cellphones_page_locators import *


class CellPhone(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver= driver)

    def add_htc_m8one_android_lollipop_to_cart(self):
        self.click_element(link_htc_m8one_android_lollipop)
        self.click_element(button_add_to_cart_htc_m8one_android_lollipop)

    def add_htc_m8one_android_lollipop_to_compare_list(self):
        self.click_element(link_htc_m8one_android_lollipop)
        self.click_element(button_add_to_compare_list_htc_m8one_android_lollipop)

    def add_htc_m8one_android_lollipop_to_wishlist(self):
        self.click_element(link_htc_m8one_android_lollipop)
        self.click_element(button_add_to_compare_list_htc_m8one_android_lollipop)

    def add_htc_one_mini_blue_to_cart(self):
        self.click_element(link_htc_one_mini_blue)
        self.click_element(button_add_to_cart_htc_one_mini_blue)

    def add_htc_one_mini_blue_to_compare_list(self):
        self.click_element(link_htc_one_mini_blue)
        self.click_element(button_add_to_compare_list_htc_one_mini_blue)

    def add_htc_one_mini_blue_to_wishlist(self):
        self.click_element(link_htc_one_mini_blue)
        self.click_element(button_add_to_wishlist_htc_one_mini_blue)

    def add_nokia_lumia_to_cart(self):
        self.click_element(link_nokia_lumia)
        self.click_element(button_add_to_cart_nokia_lumia)

    def add_nokia_lumia_to_compare_list(self):
        self.click_element(link_nokia_lumia)
        self.click_element(button_add_to_compare_list_nokia_lumia)

    def add_nokia_lumia_to_wishlist(self):
        self.click_element(link_nokia_lumia)
        self.click_element(button_add_to_wishlist_nokia_lumia)

