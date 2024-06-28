from selenium.webdriver.common.by import By
from base.SeleniumBaseClass import SeleniumBase
from base.SeleniumBaseClass import SeleniumBase
#locators

link_camera_and_photos = (By.PARTIAL_LINK_TEXT,"Camera & photo")
link_cell_phone = (By.PARTIAL_LINK_TEXT,"Cell phones")
link_others  = (By.PARTIAL_LINK_TEXT,"Others")

#cell_phone_product locators
link_cell_phones = (By.PARTIAL_LINK_TEXT,"Cell phones")
link_htc_one_mini_blue = (By.PARTIAL_LINK_TEXT,"HTC One Mini Blue")
btn_add_cellphone_pdt_to_cart=(By.XPATH,"//button[@class='button-2 product-box-add-to-cart-button']")



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


