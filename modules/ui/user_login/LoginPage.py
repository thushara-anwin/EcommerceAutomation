from base.SeleniumBaseClass import SeleniumBase
from modules.ui.user_login.user_login_page_locator import *
from modules.ui.user_login.login_page_data import *


class Login(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver=driver)

    def click_link_login(self):
        self.click_element(link_login)

    def enter_valid_id_to_text_box_email_id(self):
        self.enter_value(valid_id,text_box_email_id)

    def enter_invalid_id_to_text_box_email_id(self):
        self.enter_value(invalid_id,text_box_email_id)

    def enter_no_value_to_text_box_email_id(self):
        self.enter_value("",text_box_email_id)

    def enter_valid_pswd_to_text_box_password(self):
        self.enter_value(valid_password, text_box_password)

    def enter_invalid_pswd_to_text_box_password(self):
        self.enter_value(invalid_password, text_box_password)

    def enter_no_value_to_text_box_password(self):
        self.enter_value("", text_box_password)

    def click_button_login(self):
        self.click_element(button_login)

    def get_logout_element(self):
        element = self.get_element(link_log_out)
        return element

    def click_logout(self):
        self.click_element(link_log_out)
    def get_warning_email_error(self):
        element = self.get_element(warning_email_error)
        return element

    def get_warning_invalid_credentials(self):
        element = self.get_element(warning_invalid_credentials)
        return element



    def user_login(self):
        self.click_link_login()
        self.enter_valid_id_to_text_box_email_id()
        self.enter_valid_pswd_to_text_box_password()
        self.click_button_login()


