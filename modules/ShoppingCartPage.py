from selenium.webdriver.common.by import By
from base.SeleniumBaseClass import SeleniumBase

#locators
link_shopping_cart = (By.PARTIAL_LINK_TEXT,"Shopping cart")
items_list = (By.CSS_SELECTOR,"button.remove-btn")
check_box_terms_of_service =(By.CSS_SELECTOR,"input#termsofservice")
message_shopping_cart_empty = (By.XPATH,"//div[contains(text(),'Your Shopping Cart is empty!')]")
button_checkout = (By.CSS_SELECTOR,"button#checkout")

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


