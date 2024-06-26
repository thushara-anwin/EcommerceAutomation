from selenium.webdriver.common.by import By
from base.SeleniumBaseClass import SeleniumBase
homepage_url = "https://demo.nopcommerce.com/"

# homepage _locators
textbox_search =(By.ID,"small-searchterms")
btn_search=(By.XPATH,"//button[@type='submit']")
title_locator =(By.XPATH,"//title[text()='nopCommerce demo store']")
link_login =(By.LINK_TEXT,"Log in")
link_register =(By.LINK_TEXT,"Register")
link_wishlist =(By.XPATH,"//span[text()='Wishlist']")
valid_product_locator=(By.XPATH,"//button[text()='Add to cart']")
no_product_message=(By.XPATH,"//div[@class='no-result']")
min_length_warning_locator =(By.XPATH,"//div[@class='warning']")

# homepage_data
valid_search_data ="Apple MacBook Pro 13-inch"
invalid_search_data="good morning"
short_search_data ="hi"

homepage_title ="nopCommerce demo store"

#product_category_locators
link_computers= (By.PARTIAL_LINK_TEXT,"Computers")
link_desktops = (By.PARTIAL_LINK_TEXT,"Desktops")
link_notebooks = (By.PARTIAL_LINK_TEXT,"notebooks")



link_electronics= (By.PARTIAL_LINK_TEXT,"Electronics")
link_camera_and_photo = (By.PARTIAL_LINK_TEXT,"Camera & photo")
link_cell_phones =(By.PARTIAL_LINK_TEXT,"Cell phones")
link_electronics_others =(By.PARTIAL_LINK_TEXT,"Cell phones")


link_apparel= (By.PARTIAL_LINK_TEXT,"Apparel")
link_shoes = (By.PARTIAL_LINK_TEXT,"Shoes")
link_clothing =(By.PARTIAL_LINK_TEXT,"Clothing")
link_accessories  =(By.PARTIAL_LINK_TEXT,"Accessories")



link_digital_downloads= (By.PARTIAL_LINK_TEXT,"Digital downloads")
link_books= (By.PARTIAL_LINK_TEXT,"Books")
link_jewelry= (By.PARTIAL_LINK_TEXT,"Jewelry")
link_gift_cards= (By.PARTIAL_LINK_TEXT,"Gift Cards")
computer_products_page_title = (By.XPATH,"//h1[text()='Computers']")
electronics_products_page_title = (By.XPATH,"//h1[text()='Electronics']")
apparel_products_page_title = (By.XPATH,"//h1[text()='Apparel']")
digital_downloads_products_page_title = (By.XPATH,"//h1[text()='Digital downloads']")
books_products_page_title = (By.XPATH,"//h1[text()='Books']")
jewelry_products_page_title = (By.XPATH,"//h1[text()='Jewelry']")
gift_card_products_page_title = (By.XPATH,"//h1[text()='Gift Cards']")


class HomePage(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver=driver)

    def navigate_to_homepage(self):
        self.driver.get(homepage_url)

    def get_title(self):
        title = self.get_text(title_locator)
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

    def click_notebooks(self):
        self.get_element_mouse_hover(link_computers,link_desktops,link_notebooks)

