from base.SeleniumBaseClass import SeleniumBase
from modules.ui.jewelry.jewelry_page_locators import *


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



