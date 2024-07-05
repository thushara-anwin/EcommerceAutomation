from selenium.webdriver.common.by import By
from base.SeleniumBaseClass import SeleniumBase

#locators
link_htc_m8one_android_lollipop = (By.PARTIAL_LINK_TEXT,"HTC One M8 Android L 5.0 Lollipop")
button_add_to_cart_htc_m8one_android_lollipop=(By.CSS_SELECTOR,"button#add-to-cart-button-18")
button_add_to_wishlist_htc_m8one_android_lollipop=(By.CSS_SELECTOR,"button#add-to-wishlist-button-18")
button_add_to_compare_list_htc_m8one_android_lollipop=(By.CSS_SELECTOR,"button.button-2.add-to-compare-list-button")


link_htc_one_mini_blue = (By.PARTIAL_LINK_TEXT,"HTC One Mini Blue")
button_add_to_cart_htc_one_mini_blue=(By.CSS_SELECTOR,"button#add-to-cart-button-19")
button_add_to_wishlist_htc_one_mini_blue=(By.CSS_SELECTOR,"button#add-to-wishlist-button-19")
button_add_to_compare_list_htc_one_mini_blue=(By.CSS_SELECTOR,"button.button-2.add-to-compare-list-button")


link_nokia_lumia = (By.PARTIAL_LINK_TEXT,"Nokia Lumia 1020")
button_add_to_cart_nokia_lumia=(By.CSS_SELECTOR,"button#add-to-cart-button-20")
button_add_to_wishlist_nokia_lumia=(By.CSS_SELECTOR,"button#add-to-wishlist-button-20")
button_add_to_compare_list_nokia_lumia=(By.CSS_SELECTOR,"button.button-2.add-to-compare-list-button")


link_compare_products =(By.PARTIAL_LINK_TEXT,"Compare products list")

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

    def click_on_link_compare_products_list(self):
        self.click_element(link_compare_products)