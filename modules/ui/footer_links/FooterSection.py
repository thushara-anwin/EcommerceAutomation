from base.SeleniumBaseClass import SeleniumBase
from modules.ui.footer_links.footer_locators import *
from modules.ui.footer_links.footer_data import *
from faker import Faker
class Footer(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver=driver)
        self.fk = Faker()


    def click_on_link_contact_us(self):
        self.click_element(link_contact_us)

    def enter_fullname(self):
        self.enter_value(full_name,text_box_full_name)

    def empty_fullname(self):
        self.enter_value(empty_data,text_box_full_name)


    def enter_email(self):
        self.enter_value(email,text_box_email)

    def empty_email(self):
        self.enter_value(empty_data,text_box_email)

    def enter_enquiry(self):
        self.enter_value(enquiry, text_box_enquiry)

    def empty_enquiry(self):
        self.enter_value(empty_data, text_box_enquiry)

    # def contact_us(self):
    #     self.click_element(link_contact_us)
    #     self.enter_value(enquiry,text_box_enquiry)
    #     self.click_element(button_enquiry_submit)

    def click_submit_enquiry(self):
        self.click_element(button_enquiry_submit)

    def get_success_message_enquiry_submission(self):
        element = self.get_element(message_enquiry_submitted_successfully)
        return element

    def get_message_error_enquiry(self):
        element = self.get_element(message_error_enquiry)
        return element

    def get_message_error_full_name(self):
        element = self.get_element(message_error_full_name)
        return element

    def get_message_error_email(self):
        element = self.get_element(message_error_email)
        return element

    def click_on_link_compare_products_list(self):
        self.click_element(link_compare_products)

    def get_compare_products_title(self):
        element =self.get_element(title_compare_products_page)
        return element

    def click_on_link_new_products(self):
        self.click_element(link_new_products)

    def get_title_new_products(self):
        element =self.get_element(title_new_products_page)
        return

    def click_on_link_news(self):
        self.click_element(link_news)


    def get_title_news_page(self):
        element =self.get_element(title_news_page)
        return element





