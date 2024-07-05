from base.SeleniumBaseClass import SeleniumBase
from modules.ui.shopping_cart.shopping_cart_locators import *


class ShoppingCart(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver=driver)

    def click_on_link_shopping_cart(self):
        self.click_element(link_shopping_cart)

    def remove_items_from_the_cart(self):
        self.click_element(items_list)

    def get_message_shopping_cart_empty(self):
        element = self.get_element(message_shopping_cart_empty)
        return element

    def click_on_check_box_terms_of_service(self):
        self.click_element(check_box_terms_of_service)

    def click_on_button_checkout(self):
        self.click_element(button_checkout)





