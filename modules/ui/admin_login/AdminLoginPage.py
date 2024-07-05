from base.SeleniumBaseClass import SeleniumBase
from modules.ui.admin_login.admin_login_page_locators import *
from modules.ui.admin_login.admin_login_page_data import *



class Admin(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver=driver)

    def navigate_to_admin_page_url(self):
        self.driver.get(admin_page_url)

    def enter_valid_admin_email(self):
        self.enter_value(valid_admin_email,textbox_admin_email)

    def enter_invalid_admin_email(self):
        self.enter_value(invalid_admin_email,textbox_admin_email)

    def enter_valid_admin_password(self):
        self.enter_value(valid_admin_pass,textbox_admin_password)

    def enter_invalid_admin_password(self):
        self.enter_value(invalid_admin_pass,textbox_admin_password)

    def click_login(self):
        self.click_element(btn_login)

    def click_logout(self):
        self.click_element(btn_logout)

    def get_admin_page_title(self):
        element = self.get_element(admin_page_title)
        title = element.text
        return title

    def get_invalid_user_warning(self):
        element = self.get_element(invalid_user_warning)
        title = element.text
        return title

    def get_invalid_password_warning(self):
        element = self.get_element(invalid_password)
        title = element.text
        return title

    def get_no_credential_warning(self):
        element = self.get_element(no_credentials)
        title = element.text
        return title




