from selenium.webdriver.common.by import By
from base.SeleniumBaseClass import SeleniumBase
#admin_page_url
admin_page_url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
#locators

textbox_admin_email = (By.ID,"Email")
textbox_admin_password = (By.ID,"Password")
btn_login = (By.XPATH,"//button[@type='submit']")
admin_page_title = (By.XPATH,"//h1[contains(text(),'Dashboard')]")
invalid_user_warning =(By.XPATH,"//li")
invalid_password= (By.XPATH,"//li")
no_credentials = (By.CSS_SELECTOR,"span#Email-error")
btn_logout = (By.LINK_TEXT,"Logout")


# data
valid_admin_email = "admin@yourstore.com"
invalid_admin_email = "123admin@yourstore.com"
valid_admin_pass="admin"
invalid_admin_pass="admin123"

# titles and messages
admin_page_title_text = "Dashboard"
invalid_user_warning_message = "No customer account found"
invalid_password_warning_message = "The credentials provided are incorrect"
no_credentials_warning_message = "Please enter your email"


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




