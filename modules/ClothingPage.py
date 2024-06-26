from selenium.webdriver.common.by import By
from base.SeleniumBaseClass import SeleniumBase
#clothing_page_url
#clothing_page_url ="https://demo.nopcommerce.com/clothing"
custom_t_shirt = (By.PARTIAL_LINK_TEXT,"Custom T-Shirt")

custom_t_shirt_name =(By.XPATH,"//h1[text()='Custom T-Shirt']")
custom_t_shirt_price =(By.ID,"price-value-29")
custom_t_shirt_description = (By.XPATH,"//div[@class='full-description']")
class ClothingPage(SeleniumBase):
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

