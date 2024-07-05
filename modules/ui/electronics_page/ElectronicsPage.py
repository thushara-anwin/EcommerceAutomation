
from base.SeleniumBaseClass import SeleniumBase
from modules.ui.electronics_page.electronics_page_locators import *

class Electronics(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver=driver)

    def click_on_link_camera_and_photos(self):
        self.click_element(link_camera_and_photos)

    def click_on_link_cellphone(self):
        self.click_element(link_cell_phone)

    def click_cell_phones(self):
        self.click_element(link_cell_phones)

    def click_htc_one_mini_blue(self):
        self.click_element(link_htc_one_mini_blue)

    def add_cellphone_pdts_to_cart(self):
        self.click_element(btn_add_cellphone_pdt_to_cart)


    def click_on_link_others(self):
        self.click_element(link_others)


