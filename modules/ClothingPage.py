from selenium.webdriver.common.by import By
from base.SeleniumBaseClass import SeleniumBase
#clothing_page_url
#clothing_page_url ="https://demo.nopcommerce.com/clothing"
custom_t_shirt = (By.PARTIAL_LINK_TEXT,"Custom T-Shirt")
nike_tailwind_short_sleeve_running_shirt = (By.PARTIAL_LINK_TEXT,"Nike Tailwind Loose Short-Sleeve Running Shirt")
Levi_511_jeans = (By.PARTIAL_LINK_TEXT,"Levi's 511 Jeans")



custom_t_shirt_name =(By.XPATH,"//h1[text()='Custom T-Shirt']")
custom_t_shirt_price =(By.ID,"price-value-29")
custom_t_shirt_description = (By.XPATH,"//div[@class='full-description']")
custom_tshirt_code = (By.CSS_SELECTOR,"sku-29")
text_box_custom_tshirt_code =(By.CSS_SELECTOR,"input#product_attribute_12")
button_custom_tshirt_add_to_cart =(By.CSS_SELECTOR,"button#add-to-cart-button-29")
button_custom_tshirt_add_to_wishlist =(By.CSS_SELECTOR,"button#add-to-wishlist-button-29")
button_nike_tailwind_short_sleeve_running_shirt_add_to_wishlist =(By.CSS_SELECTOR,"button#add-to-wishlist-button-27")
button_Levi_511_jeans_add_to_wishlist =(By.CSS_SELECTOR,"button#add-to-wishlist-button-30")
#remove_Levi_511_jeans_from_wishlist = (By.CSS_SELECTOR,"input#removefromcart11229")
remove_Levi_511_jeans_from_wishlist = (By.CSS_SELECTOR,"button.remove-btn")
message_wishlist_empty = (By.CSS_SELECTOR,"div.no-data")




class Clothing(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver=driver)

    def click_custom_t_shirt(self):
        self.click_element(custom_t_shirt)

    def get_custom_t_shirt_name(self):
        element = self.get_element(custom_t_shirt_name)
        return element

    def get_custom_t_shirt_price(self):
        element = self.get_element(custom_t_shirt_price)
        return element

    def get_custom_t_shirt_description(self):
        element = self.get_element(custom_t_shirt_description)
        return element

    def click_add_to_cart(self):
        self.click_element(button_custom_tshirt_add_to_cart)

    def add_nike_tailwind_short_sleeve_running_shirt_to_wishlist(self):
        self.click_element(nike_tailwind_short_sleeve_running_shirt)
        self.click_element(button_nike_tailwind_short_sleeve_running_shirt_add_to_wishlist)

    def add_custom_tshirt_to_wishlist(self):
        self.click_element(custom_t_shirt)
        self.click_element(button_custom_tshirt_add_to_wishlist)

    def add_levi_511_jeans_to_wishlist(self):
        self.click_element(Levi_511_jeans)
        self.click_element(button_Levi_511_jeans_add_to_wishlist)

    def remove_levi_511_jeans_from_wishlist(self):
        self.click_element(remove_Levi_511_jeans_from_wishlist)

    def get_wishlist_empty_message(self):
        element = self.get_element(message_wishlist_empty)
        return element


    # def add_custom_tshirt_to_cart(self):
    #     self.click_element(custom_t_shirt)
    #     element = self.get_element(custom_tshirt_code)
    #     code=element.text
    #     self.enter_value(code,text_box_custom_tshirt_code)
    #     self.click_element(button_custom_tshirt_add_to_cart)


