from selenium.webdriver.common.by import By
from base.SeleniumBaseClass import SeleniumBase

#jewelry products locators
link_flower_girl_bracelet = (By.PARTIAL_LINK_TEXT,"Flower Girl Bracelet")
add_flower_girl_bracelet_to_cart = (By.CSS_SELECTOR,"button#add-to-cart-button-41")


link_vintage_style_engagement_ring = (By.PARTIAL_LINK_TEXT,"Vintage Style Engagement Ring")
add_vintage_style_engagement_ring_to_cart = (By.CSS_SELECTOR,"button#add-to-cart-button-42")

class Jewelry(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver=driver)

    def click_on_link_flower_girl_bracelet(self):
        self.click_element(link_flower_girl_bracelet)

    def add_flower_girl_bracelet_to_cart(self):
        self.click_element(link_flower_girl_bracelet)
        self.click_element(add_flower_girl_bracelet_to_cart)

    def click_on_link_vintage_style_engagement_ring(self):
        self.click_element(link_vintage_style_engagement_ring)

    def add_vintage_style_engagement_ring_to_cart(self):
        self.click_element(link_vintage_style_engagement_ring)
        self.click_element(add_vintage_style_engagement_ring_to_cart)



