import pytest
from modules.AdminLoginPage import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.ap = Admin(self.driver)
        self.ap.navigate_to_admin_page_url()

    def test_login_with_valid_credentials(self):
        self.ap.enter_valid_admin_email()
        self.ap.enter_valid_admin_password()
        self.ap.click_login()
        text= self.ap.get_admin_page_title()
        #assert text.__eq__(admin_page_title_text)
        if text == admin_page_title_text:
            self.ap.click_logout()
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\login_failure.png")
            assert False


    def test_login_with_invalid_user(self):
        self.ap.enter_invalid_admin_email()
        self.ap.enter_valid_admin_password()
        self.ap.click_login()

        text = self.ap.get_invalid_user_warning()
        if text == invalid_user_warning_message:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\invalid_user.png")
            assert False

    def test_login_with_invalid_password(self):
        self.ap.enter_valid_admin_email()
        self.ap.enter_invalid_admin_password()
        self.ap.click_login()
        text = self.ap.get_invalid_password_warning()
        if text == invalid_password_warning_message:
            assert True
        else:
            assert False



